from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese Contraseña'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese Contraseña Repetida'
            }
        )
    )
    
    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'first_name',
            'last_name',
            'gender',
        )
        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')
        elif len(self.cleaned_data['password2']) < 4:
            self.add_error('password2', 'La contraseña debe ser mayor a 3 dígitos')
            
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre de usuario',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario son incorrectos')
        
        return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):
    
    username1 = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre de usuario',
            }
        )
    )

    password1 = forms.CharField(
        label='Contraseña Actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese Contraseña Actual'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese Contraseña Nueva'
            }
        )
    )
    
    password3 = forms.CharField(
        label='Repetir Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese Contraseña Repetida'
            }
        )
    )
    
    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        
        username1 = self.cleaned_data['username1']
        password1 = self.cleaned_data['password1']
        
        if not authenticate(username=username1, password=password1):
            raise forms.ValidationError('La contraseña o el usuario actual no son correctos')
    
        return self.cleaned_data
    
    
    def clean_password3(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password3']:
            self.add_error('password3', 'Las contraseñas no coinciden')
        elif len(self.cleaned_data['password2']) < 4:
            self.add_error('password2', 'La contraseña debe ser mayor a 3 dígitos')
    
class VerificationForm(forms.Form):
    registration_code = forms.CharField(required=True)

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_registration_code(self):
        code = self.cleaned_data['registration_code']

        if len(code) == 4:
            # verificamos si el codigo y el id de usuario son validos:
            active = User.objects.cod_validation(
                self.id_user,
                code
            )
            if not active:
                raise forms.ValidationError('Él codigo de verificación es incorrecto')
        else:
            raise forms.ValidationError('Él codigo de verificación es incorrecto')
        