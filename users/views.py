# Django classes
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


# Models
from django.contrib.auth import get_user_model

User = get_user_model()

# Forms
from users.forms import SignupForm


def login_view(request):
    """Login view."""
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Usuario o contraseña invalidos'})
    return render(request, 'users/login.html')

@permission_required(('user.is_authenticated','user.is_superuser'))
def signup_view(request):
    """Sign up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.last()
            messages.success(request, 'El perfil de '+user.username+' fue creado con exito')
            return redirect('user:detail', username=user.username )
    else:
        form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form':form}
    )

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('user:login')


class UserDetailView(LoginRequiredMixin, DetailView):
    """User Detail View."""
    template_name = "users/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()


class HomeView(PermissionRequiredMixin, TemplateView):
    """Home view from users module."""
    permission_required = ('user.is_authenticated', 'user.is_superuser')
    template_name = 'users/home.html'


class UsersListView(PermissionRequiredMixin, ListView):
    """List view from all users."""
    permission_required = ('user.is_authenticated', 'user.is_superuser')
    model = User
    context_object_name = 'users'
    template_name = 'users/list_users.html'

class UserDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    """Delete user."""
    permission_required = ('user.is_authenticated', 'user.is_superuser')
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('user:home')
    success_message = 'Perfil eliminado satisfactoriamente'
    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(UserDeleteView,self).delete(request, *args, **kwargs)