from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings


urlpatterns = [
    path('', include('inicio.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'core.views.error_404'