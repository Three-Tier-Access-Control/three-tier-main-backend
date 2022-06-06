from django.urls import path, include
from rest_framework import routers

from access.views import AccessLogViewSet


router = routers.DefaultRouter()
router.register(r'', AccessLogViewSet)


urlpatterns = [
    path('', include(router.urls)),
]