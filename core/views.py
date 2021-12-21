
from django.shortcuts import redirect, render



def error_404(request, exception):
        data = {}
        return render(request,'inicio/404.html', data)
