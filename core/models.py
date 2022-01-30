from django.db import models

# Create your models here.

class LocationEntry(models.Model):
    #{"_type": "location", "acc": 5, "alt": 112, "batt": 79, "bs": 1, "conn": "m", "created_at": 1643461134, "inregions": ["home"], "lat": 31.2375869, "lon": 34.3562222, "t": "u", "tid": "go", "topic": "owntracks/user/ginkgo", "tst": 1643461122, "vac": 1, "vel": 0}
    #{"_type": "location", "BSSID": "30:b5:c2:e9:f4:2a", "SSID": "TP-LINK_E9F42A", "acc": 4, "alt": 112, "batt": 64, "bs": 1, "conn": "w", "created_at": 1643483730, "inregions": ["home"], "lat": 31.237657, "lon": 34.3561878, "t": "u", "tid": "go", "topic": "owntracks/user/ginkgo", "tst": 1643483730, "vac": 1, "vel": 6}
    _type = models.CharField(max_length=255, blank=True, null=True)
    BSSID = models.CharField(max_length=255, blank=True, null=True)
    SSID = models.CharField(max_length=255, blank=True, null=True)
    acc = models.IntegerField(blank=True, null=True)
    alt = models.IntegerField(blank=True, null=True)
    batt = models.IntegerField(blank=True, null=True)
    bs = models.IntegerField(blank=True, null=True)
    conn = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    inregions = models.ManyToManyField(to='WaypointEntry') #models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    t = models.CharField(max_length=255, blank=True, null=True)
    tid= models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    tst = models.IntegerField(blank=True, null=True)
    vac = models.IntegerField(blank=True, null=True)
    vel = models.IntegerField(blank=True, null=True)
    dcreated_at = models.DateTimeField(auto_now_add=True)
    dtst = models.DateTimeField(blank=True, null=True)

    def inregions_display(self):
        return ', '.join([p.desc for p in self.inregions.all()])

class WaypointEntry(models.Model):
    #{"_type": "waypoint", "desc": "home", "lat": 31.2376273, "lon": 34.3561845, "rad": 10, "topic": "owntracks/user/ginkgo/waypoints", "tst": 1643460966}
    _type = models.CharField(max_length=255, blank=True, null=True)
    desc = models.CharField(max_length=255, unique=True,)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    rad = models.IntegerField(blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    tst = models.IntegerField(blank=True, null=True)
    dcreated_at = models.DateTimeField(auto_now_add=True)
    dtst = models.DateTimeField(blank=True, null=True)

class TransitionEntry(models.Model):
    # {"_type": "transition", "acc": 31.696, "desc": "home", "event": "enter", "lat": 31.2376435, "lon": 34.3562534, "t": "l", "tid": "go", "topic": "owntracks/user/ginkgo/event", "tst": 1643460988, "wtst": 1643460966}
    _type = models.CharField(max_length=255, blank=True, null=True)
    acc = models.FloatField(blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    t = models.CharField(max_length=255, blank=True, null=True)
    tid = models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    tst = models.IntegerField(blank=True, null=True)
    wtst = models.IntegerField(blank=True, null=True)
    dcreated_at = models.DateTimeField(auto_now_add=True)
    dtst = models.DateTimeField(blank=True, null=True)


class LocationEntryJson(models.Model):
    data = models.JSONField(blank=True, null=True)
    dcreated_at = models.DateTimeField(auto_now_add=True)
    dtst = models.DateTimeField(blank=True, null=True)


class WayPointsEntry(models.Model):
    # {'_type': 'waypoints', 'topic': 'owntracks/user/ginkgo/waypoints', 'waypoints': [{'_type': 'waypoint', 'desc': 'home', 'lat': 31.2376273, 'lon': 34.3561845, 'rad': 10, 'tst': 1643460966}]}
    _type = models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    waypoints = models.ManyToManyField(to=WaypointEntry)