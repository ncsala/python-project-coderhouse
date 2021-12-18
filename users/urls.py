from django.urls.conf import path
from .views import *


urlpatterns = [
    path('registro/', UserRegisterView.as_view(), name='url-registro-usuario'),
    path('login/', LoginUser.as_view(), name='url-login-usuario'),
    path('logout/', LogoutView.as_view(), name='url-logout-usuario'),
    path('profile/', UserProfile.as_view(), name='url-profile-usuario'),
    path('pwd-update/', UpdatePasswordView.as_view(), name='url-update-pwd-usuario'),
    path('verification/<pk>/', CodeVerificationView.as_view(), name='url-verification'),
]