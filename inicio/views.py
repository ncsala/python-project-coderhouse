from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView


def HomeView(request):
    # Vista que carga la pagina de inicio
    return render(request,'inicio/index.html', {})

class AboutView(TemplateView):
    template_name = "inicio/about.html"
    