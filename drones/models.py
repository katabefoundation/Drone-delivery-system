from django.db import models


# Create your models here.
class Drone(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='inactive')  # 'inactive', 'active', 'maintenance'
    battery_percentage = models.IntegerField(default=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name