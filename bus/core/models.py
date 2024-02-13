from django.db import models
import uuid

# Create your models here.
class Standard(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Bus(Standard):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=255, null=False)
    plate = models.CharField(max_length=7, null=False)
    available_seats = models.IntegerField()
    last_station = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'