from rest_framework.routers import DefaultRouter

from .views import TravelViewSet

router = DefaultRouter()
router.register('travels', TravelViewSet, basename='travels')