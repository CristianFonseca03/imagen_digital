"""Imagen digital views"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
User = get_user_model()

class Home_view(LoginRequiredMixin,TemplateView):
    """Home view."""
    template_name = 'imagen_digital/home.html'