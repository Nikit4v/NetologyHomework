import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from app.models import Station, Route


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', 'r') as csvfile:

            csv_reader = csv.DictReader(csvfile, delimiter=';')

            for line in csv_reader:
                station = Station()
                station.latitude = line["Latitude_WGS84"]
                station.longitude = line["Longitude_WGS84"]
                station.name = line["Name"]
                string = line["RouteNumbers"].split(";")
                station.save()
                for i in range(len(string)):
                    route = Route()
                    route.name = string[i].replace(" ", "")
                    route.save()
                    station.routes.add(route)
                station.save()
                del string
