from datetime import datetime
from django.db import models
import uuid

# Create your models here.
class Standard(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Travel(Standard):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    category = models.CharField(max_length=255, null=False)
    origin = models.CharField(max_length=255, null=False)
    destination = models.CharField(max_length=255, null=False)
    departure = models.TimeField()
    arrival = models.TimeField()
    forecast = models.TimeField(editable=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Travel'
        verbose_name_plural = 'Travels'
        ordering = ['id']

    def save(self, *args, **kwargs):
        try:
            departure = datetime.combine(datetime.now().date(), datetime.strptime(self.departure, "%H:%M:%S").time())
            arrival = datetime.combine(datetime.now().date(), datetime.strptime(self.arrival, "%H:%M:%S").time())
        except:
            departure = datetime.combine(datetime.now().date(), self.departure)
            arrival = datetime.combine(datetime.now().date(), self.arrival)
        duration = arrival - departure
        forecast = datetime(1, 1, 1, 0, 0, 0) + duration
        self.forecast = forecast.time()
        super(Travel, self).save(*args, **kwargs)