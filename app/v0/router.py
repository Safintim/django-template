from rest_framework.routers import DefaultRouter
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


router = DefaultRouter()
router.register(r'devices', FCMDeviceAuthorizedViewSet, basename='devices')

