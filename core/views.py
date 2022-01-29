from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import LocationEntryJson, LocationEntry, TransitionEntry, WaypointEntry
from datetime import datetime
import nacl.secret
import nacl.utils
from cryptography.fernet import Fernet
# Create your views here.
@csrf_exempt
@api_view(['POST'])
def location_ping(request):
    data = request.data
    LocationEntryJson.objects.create(data=data)
    if data.get('_type', None) == 'location':
        #{"_type": "location", "BSSID": "30:b5:c2:e9:f4:2a", "SSID": "TP-LINK_E9F42A", "acc": 4, "alt": 112, "batt": 64, "bs": 1, "conn": "w", "created_at": 1643483730, "inregions": ["home"], "lat": 31.237657, "lon": 34.3561878, "t": "u", "tid": "go", "topic": "owntracks/user/ginkgo", "tst": 1643483730, "vac": 1, "vel": 6}
        LocationEntry.objects.create(
            _type=data.get('_type', None),
            BSSID=data.get('BSSID', None),
            SSID=data.get('SSID', None),
            acc=data.get('acc', None),
            alt=data.get('alt', None),
            batt=data.get('batt', None),
            bs=data.get('bs', None),
            conn=data.get('conn', None),
            created_at=datetime.fromtimestamp(data.get('created_at', None), tz=datetime.now().tzinfo),
            inregions=data.get('inregions', None),
            lat=data.get('lat', None),
            lon=data.get('lon', None),
            t=data.get('t', None),
            tid=data.get('tid', None),
            topic=data.get('topic', None),
            tst=data.get('tst', None),
            vac=data.get('vac', None),
            vel=data.get('vel', None),
        )
    elif data.get('_type', None) == 'waypoint':
        WaypointEntry.objects.create(
            _type=data.get('_type', None),
            desc=data.get('desc', None),
            lat=data.get('lat', None),
            lon=data.get('lon', None),
            rad=data.get('rad', None),
            topic=data.get('topic', None),
            tst=data.get('tst', None),
        )
    elif data.get('_type', None) == 'transition':
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
        )
    return JsonResponse(data={
        'status':'ok',
    })