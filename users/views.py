#Django classes
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views.generic import DetailView,TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

#Models
from django.contrib.auth import get_user_model
User = get_user_model()


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
            return render(request,'users/login.html',{'error':'Usuario o contraseña invalidos'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('user:login')

class UserDetailView(LoginRequiredMixin,DetailView):
    """User Detail View"""
    template_name = "users/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()

class HomeView(PermissionRequiredMixin,TemplateView):
    """Home view from users module."""
    permission_required = ('user.is_authenticated', 'user.is_superuser')
    template_name = 'users/home.html'

class UsersListView(PermissionRequiredMixin,ListView):
    """List view from all users."""
    permission_required = ('user.is_authenticated','user.is_superuser')
    model = User
    context_object_name = 'users'
    template_name = 'users/list_users.html'