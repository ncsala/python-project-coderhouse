import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATICFILES_DIRS = [r'C:\Users\nicoe\Desktop\LOCAL-python\pythonproject\python_project\static']
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = [r'C:\Users\nicoe\Desktop\LOCAL-python\pythonproject\python_project\media']
MEDIA_ROOT = BASE_DIR / 'media'

# Configuraciones de email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'python.project.coderhouse@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587