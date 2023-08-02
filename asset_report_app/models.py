from django.db import models
from django.db import models


class VehicleData(models.Model):
    case_open = models.DateTimeField()
    harsh_acceleration = models.FloatField()
    lat = models.FloatField()
    lon = models.FloatField()
    lic_plate_no = models.CharField(max_length=20)

    def __str__(self):
        return self.lic_plate_no