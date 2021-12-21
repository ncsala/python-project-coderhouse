from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from .views import AboutView, HomeView


urlpatterns = [
    path('', HomeView, name='url-inicio'),
    path('about/', AboutView.as_view(), name='url-about'),
    path('empleados/', include('employees.urls')),
    path('departamentos/', include('department.urls')),
    path('registro-usuarios/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
