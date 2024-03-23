from django.db import models

# Create your models here.
class Travel(models.Model):
    name = models.CharField(max_length=100)
    price_confort = models.FloatField()
    price_econ = models.FloatField()
    city = models.CharField(max_length=100)
    duration = models.DurationField()
    seat = models.CharField(max_length=3)
    bed = models.CharField(max_length=3)