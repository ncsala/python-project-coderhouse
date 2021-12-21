from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
GENDER_CHOICES = (
    ('F', 'Femenino'),
    ('M', 'Masculino'),
    ('O', 'Otro'),
)

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    username = models.CharField(max_length=15, unique=True)
    # despues puedo cambiar a unique para que el mail no se repita
    email = models.EmailField()
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    registration_code = models.CharField(max_length=4, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name