"""Imagen digital views"""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

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

class Home_view(LoginRequiredMixin,TemplateView):
    """Home view."""
    template_name = 'imagen_digital/home.html'

@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')

class UserDetailView(LoginRequiredMixin,DetailView):
    """User Detail View"""
    template_name = "imagen_digital/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()