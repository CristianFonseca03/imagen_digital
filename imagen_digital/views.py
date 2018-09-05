"""Imagen digital views"""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hello')
        else:
            return render(request,'imagen_digital/login.html',{'error':'invalid username or password'})
    return render(request, 'imagen_digital/login.html')

@login_required
def HelloWorld(request):
    return HttpResponse('Hola mundo')