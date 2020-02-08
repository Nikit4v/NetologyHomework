from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=32)
    width = models.IntegerField()


class CsvPath(models.Model):
    path = models.TextField()

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        return 0
