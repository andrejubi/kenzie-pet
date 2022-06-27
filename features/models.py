from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=20, unique=True)
    animals = models.ManyToManyField("animals.Animal", related_name="features")
