from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta:
        email = forms.EmailField(help_text="please provide a valid email address")
        model = User
        fields = ["username", "email", "password1", "password2"]
