"""Imagen digital views"""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'imagen_digital/login.html',{'error':'Usuario o contraseña invalidos'})
    return render(request, 'imagen_digital/login.html')

@login_required
def HelloWorld(request):
    return HttpResponse('Hola mundo')

@method_decorator(login_required, name='dispatch')
class Home_view(TemplateView):
    """Home view."""
    template_name = 'imagen_digital/home.html'