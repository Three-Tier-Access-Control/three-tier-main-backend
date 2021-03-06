"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from access.views import AccessLogViewSet
from employees.views import EmployeeViewSet, FingerPrintViewSet, RFIDCardViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.views import UserViewSet
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

schema_view = get_schema_view(
    openapi.Info(
        title="Three Tier Main Backend REST API",
        default_version='v1',
        description="Three Tier Security Main Backend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ashleytshumba@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'rfid', RFIDCardViewSet)
router.register(r'fingerprint', FingerPrintViewSet)
router.register(r'access', AccessLogViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    re_path(r'^docs/(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/', include(router.urls), name='api-root'),
    path('', index),

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Three Tier Security"
admin.site.site_title = "Three Tier Security"
admin.site.index_title = "Three Tier Security Dashboard"
