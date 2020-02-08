from django.db.models import *


class Station(Model):
    name = CharField(max_length=32)
    latitude = FloatField()
    longitude = FloatField()
    route_numbers = ManyToManyField(related_name="stations", to="Route")


class Route(Model):
    name = CharField(max_length=32)
