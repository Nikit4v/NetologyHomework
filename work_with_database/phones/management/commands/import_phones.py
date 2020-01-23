import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')

            for line in phone_reader:
                phone = Phone()
                phone.id = int(line["id"])
                print(line["id"])
                phone.name = str(line["name"])
                print(line["name"])
                phone.image = str(line["image"])
                print(line["image"])
                phone.price = int(line["price"])
                print(line["price"])
                phone.release_date = line["release_date"]
                print(line["release_date"])
                phone.lte_exists = line["lte_exists"]
                print(line["lte_exists"])
                phone.slug = slugify(line["name"])
                print(slugify(line["name"]))
                phone.save()
