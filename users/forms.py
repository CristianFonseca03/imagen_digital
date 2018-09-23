"""User foms."""

# Django
from django import forms

# Models
from users.models import User


class SignupForm(forms.Form):
    """Sing in form"""
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    is_superuser = forms.BooleanField(required=False)

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El nombre de usuario ya esta en uso')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return data

    def save(self):
        """Create user o superuser"""
        data = self.cleaned_data
        is_superuser = data['is_superuser']
        data.pop("password_confirmation")
        data.pop("is_superuser")
        user = User.objects.create_user(**data)
        if is_superuser:
            user.is_superuser = True
            user.save()