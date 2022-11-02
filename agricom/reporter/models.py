from django.db import models


# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self) -> models.CharField:
        return self.name
