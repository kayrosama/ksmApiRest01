from rest_framework.routers import DefaultRouter
from apps.apis.views import HumanosModelViewSet

router_apps = DefaultRouter()

router_apps.register(prefix='apps', basename='apps', viewset=HumanosModelViewSet)
