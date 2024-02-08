from rest_framework.routers import DefaultRouter

from .views import StationViewSet, TravelViewSet

router = DefaultRouter()
router.register('stations', StationViewSet, basename='stations')
router.register('travels', TravelViewSet, basename='travels')