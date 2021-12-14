from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, UpdatePasswordForm, UserRegisterForm
from .models import User


# Create your views here.
class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        # generamos el codigo
        # code = code_generator()
        #
        usr = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            gender=form.cleaned_data['gender'],
            # codregistro=code
        )
        
        return super(UserRegisterView, self).form_valid(form)
        # enviar el codigo al email del user
        # asunto = 'Confirmación de email'
        # email_remitente = 'ncsala@gmail.com'
        
        # send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        # # redirigir a pantalla de valdiacion

        # return HttpResponseRedirect(
        #     reverse(
        #         'users_app:user-verification',
        #         kwargs={'pk': usr.id}
        #     )
        # )

class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = "users/user_profile.html"
    login_url = reverse_lazy('url-login-usuario')

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