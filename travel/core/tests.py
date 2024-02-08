from datetime import date, datetime, time, timedelta
from django.test import TestCase

from .models import Station, Travel

# Create your tests here.
class TravelTestCase(TestCase):
    def setUp(self):
        a1 = Station.objects.create(name='São Paulo (Rod. Tietê) (SP)', city='São Paulo', state='SP')
        a2 = Station.objects.create(name='Rio de Janeiro (Campo Grande) (RJ)', city='Rio de Janeiro', state='RJ')

        Travel.objects.create(departure_date=date(2024, 1, 7), arrival_date=date(2024, 1, 8), category='Executivo',
            origin=a1, destination=a2, departure_time=time(23, 0, 0), arrival_time=time(4, 0, 0), price=80.00)
        Travel.objects.create(departure_date=date(2024, 1, 7), arrival_date=date(2024, 1, 8), category='Convencional',
            origin=a1, destination=a1, departure_time=time(23, 0, 0), arrival_time=time(4, 0, 0), price=80.00)

    def test_forecast(self):
        a = Travel.objects.get(category='Executivo')
        forecast_time = timedelta(hours=5)
        self.assertEqual(a.forecast, forecast_time)

    def test_valid_travel(self):
        a1 = Station.objects.get(name='São Paulo (Rod. Tietê) (SP)')
        a2 = Station.objects.get(name='Rio de Janeiro (Campo Grande) (RJ)')
        t = Travel.objects.get(origin=a1, destination=a2)
        self.assertTrue(t.is_valid_travel())

    def test_invalid_travel_destination(self):
        a1 = Station.objects.get(name='São Paulo (Rod. Tietê) (SP)')
        t = Travel.objects.get(origin=a1, destination=a1)
        self.assertFalse(t.is_valid_travel())
