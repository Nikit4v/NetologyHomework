from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    lte_exists = models.BooleanField(blank=True, null=True)
    slug = models.SlugField("slug", unique=True, blank=True, null=True)
