from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .functions import code_generator
from .forms import *
from .models import *


# Create your views here.
class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        # Se genera el codigo para enviar a usuario nuevo
        code = code_generator()
        
        usr = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            gender=form.cleaned_data['gender'],
            registration_code = code
        )
        
        # return super(UserRegisterView, self).form_valid(form)
    
        # Envia codigo al email del usuario
        subject = 'Activación de cuenta'
        message = f'Su código de verificación es: {code}'
        sender_email = 'python.project.coderhouse@gmail.com'
        
        send_mail(subject, message, sender_email, [form.cleaned_data['email'],])

        # Redirigir a pantalla de validacion
        return HttpResponseRedirect(
            reverse(
                'url-verification',
                kwargs={'pk': usr.id}
            )
        )

class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = "users/user_profile.html"
    login_url = reverse_lazy('url-login-usuario')
    
class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail_user.html'

class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('url-inicio')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        
        return super(LoginUser, self).form_valid(form)

class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'url-inicio'
            )
        )
        
class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('url-login-usuario')
    login_url = reverse_lazy('url-login-usuario')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)

class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('url-login-usuario')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        User.objects.filter(id=self.kwargs['pk']).update(is_active=True)
        
        return super(CodeVerificationView, self).form_valid(form)
    
class UsersUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/editar_user.html'
    model = User
    login_url = reverse_lazy('url-login-usuario')
    
    fields = [
            'username',
            'first_name', 
            'last_name', 
            'gender',
            ]
    
    success_url = reverse_lazy('url-profile-usuario')
    
