from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from server.config import LOCATION_ENCRYPTION_KEY
from .models import LocationEntryJson, LocationEntry, TransitionEntry, WayPointsEntry, WaypointEntry
from datetime import datetime, timezone
import nacl.secret
import nacl.utils
from cryptography.fernet import Fernet
from nacl.encoding import Base64Encoder
from nacl.secret import SecretBox
import json

def get_cipher():
    """Return decryption function and length of key.
    Async friendly.
    """

    def decrypt(ciphertext, key):
        """Decrypt ciphertext using key."""
        return SecretBox(key).decrypt(ciphertext, encoder=Base64Encoder)

    return (SecretBox.KEY_SIZE, decrypt)

def create_LocationEntryJson(data):
    dtst = None
    if(data.get('tst', None)):
        dtst = datetime.fromtimestamp(data['tst'], timezone.utc)
    return LocationEntryJson.objects.create(data=data,dtst=dtst)

def create_LocationEntry(data):
    created_at_var = None
    if data.get('created_at', None) != None:
        created_at_var = datetime.fromtimestamp(data.get('created_at', None), timezone.utc)
    #{"_type": "location", "BSSID": "30:b5:c2:e9:f4:2a", "SSID": "TP-LINK_E9F42A", "acc": 4, "alt": 112, "batt": 64, "bs": 1, "conn": "w", "created_at": 1643483730, "inregions": ["home"], "lat": 31.237657, "lon": 34.3561878, "t": "u", "tid": "go", "topic": "owntracks/user/ginkgo", "tst": 1643483730, "vac": 1, "vel": 6}
    ret = LocationEntry.objects.create(
        _type=data.get('_type', None),
        BSSID=data.get('BSSID', None),
        SSID=data.get('SSID', None),
        acc=data.get('acc', None),
        alt=data.get('alt', None),
        batt=data.get('batt', None),
        bs=data.get('bs', None),
        conn=data.get('conn', None),
        created_at=created_at_var,
        lat=data.get('lat', None),
        lon=data.get('lon', None),
        t=data.get('t', None),
        tid=data.get('tid', None),
        topic=data.get('topic', None),
        tst=data.get('tst', None),
        vac=data.get('vac', None),
        vel=data.get('vel', None),
        dtst=datetime.fromtimestamp(data.get('tst', None), timezone.utc),
    )
    if data.get('inregions', None):
        ret.inregions.set([get_waypoint_from_string(entry) for entry in data.get('inregions', None)])
    ret.save()
    return ret
def get_waypoint_from_string(waypoint_string):
    ret = WaypointEntry.objects.get_or_create(desc=waypoint_string)
    return ret[0]
def create_WaypointEntry(data):
    ret, is_created = WaypointEntry.objects.get_or_create(desc=data.get('desc', None))
    ret._type = data.get('_type', None)
    ret.lat =data.get('lat', None)
    ret.lon =data.get('lon', None)
    ret.rad =data.get('rad', None)
    ret.topic =data.get('topic', None)
    ret.tst =data.get('tst', None)
    ret.dtst =datetime.fromtimestamp(data.get('tst', None), timezone.utc)
    ret.save()
    return ret
# Create your views here.
def create_WayPointsEntry(data):
    obj = WayPointsEntry.objects.create(
            _type=data.get('_type', None),
            topic= data.get('topic', None),
    )
    waypoints = [create_WaypointEntry(waypoint) for waypoint in data.get('waypoints', None)]
    obj.waypoints.add(*waypoints)


def create_TransitionEntry(data):
    #{"_type": "transition", "acc": 31.696, "desc": "home", "event": "enter", "lat": 31.2376435, "lon": 34.3562534, "t": "l", "tid": "go", "topic": "owntracks/user/ginkgo/event", "tst": 1643460988, "wtst": 1643460966}
    TransitionEntry.objects.create(
        _type=data.get('_type', None),
        acc=data.get('acc', None),
        desc=data.get('desc', None),
        event=data.get('event', None),
        lat=data.get('lat', None),
        lon=data.get('lon', None),
        t=data.get('t', None),
        tid=data.get('tid', None),
        topic=data.get('topic', None),
        tst=data.get('tst', None),
        wtst=data.get('wtst', None),
        dtst=datetime.fromtimestamp(data.get('tst', None), timezone.utc),
    )

@csrf_exempt
@api_view(['POST'])
def location_ping(request):
    data = request.data
    print('raw data: ', data)

    # Decrypt the data
    # https://github.com/home-assistant/core/blob/3825f80a2dd087ae70654079cd9f3071289b8423/homeassistant/components/owntracks/messages.py#L292-L320
    keylen, decrypt = get_cipher()
    key = LOCATION_ENCRYPTION_KEY
    key = key.encode("utf-8")
    key = key[:keylen]
    key = key.ljust(keylen, b"\0")
    ciphertext = data['data']
    message = decrypt(ciphertext, key)
    message = message.decode("utf-8")
    data = json.loads(message)

    print('cipher data: ', data)
    create_LocationEntryJson(data)
    if data.get('_type', None) == 'location':
        create_LocationEntry(data)
    elif data.get('_type', None) == 'waypoint':
        create_WaypointEntry(data)
    elif data.get('_type', None) == 'waypoints':
        create_WayPointsEntry(data)
    elif data.get('_type', None) == 'transition':
        create_TransitionEntry(data)

    return JsonResponse(data={
        'status':'ok',
    })