# Django classes
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.urls import reverse_lazy, reverse
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

@login_required
def change_password_view(request,username):
    """Change password view."""
    if request.user.username != username and not request.user.is_superuser:
        return render(request, '403.html')
    if request.method == 'POST':
        username_exists = User.objects.filter(username=username).exists()
        if not username_exists:
            messages.error(request,"El usuario "+username+" no existe")
            return redirect('user:home')
        user = User.objects.get(username=username)
        new_password = request.POST['new_password']
        new_password_conf = request.POST['new_password_conf']
        if new_password != new_password_conf:
            return render(request, 'users/change_password.html', {'error': 'Las contraseñas no coinciden'})
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Contraseña modificada con exito')
        return redirect('user:update', username=user.username)
    return render(request,'users/change_password.html')

@permission_required(('user.is_authenticated', 'user.is_superuser'))
def signup_view(request):
    """Sign up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.last()
            messages.success(request, 'El perfil de ' + user.username + ' fue creado con exito')
            return redirect('user:detail', username=user.username)
    else:
        form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
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


class UserDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete user."""
    permission_required = ('user.is_authenticated', 'user.is_superuser')
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('user:home')
    success_message = 'Perfil eliminado satisfactoriamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UserDeleteView, self).delete(request, *args, **kwargs)


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update user"""
    model = User
    fields = ['first_name', 'last_name', 'is_superuser']
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'users/update_user.html'
    success_message = 'Perfil editado satisfactoriamente'
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.username
        return reverse('users:detail', kwargs={'username': username})