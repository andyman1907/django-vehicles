from django.conf.urls import url, include
from . import views

from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'brand', views.BrandViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]