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


class Station(Standard):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=2, null=False)

    class Meta:
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class Travel(Standard):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    category = models.CharField(max_length=255, null=False)
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    forecast = models.DurationField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    bus = models.UUIDField(editable=True)

    class Meta:
        verbose_name = 'Travel'
        verbose_name_plural = 'Travels'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} : {self.origin} to {self.destination}'

    def is_valid_travel(self):
        return self.origin != self.destination and self.forecast.total_seconds() > 0

    def calculate_forecast(self):
        departure_datetime = datetime.combine(self.departure_date, self.departure_time)
        arrival_datetime = datetime.combine(self.arrival_date, self.arrival_time)

        return arrival_datetime - departure_datetime

    def save(self, *args, **kwargs):
        self.forecast = self.calculate_forecast()

        super(Travel, self).save(*args, **kwargs)