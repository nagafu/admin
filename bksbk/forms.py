from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from bksbk.models import User
#from django.contrib.auth import get_user_model User = get_user_model()
from django.contrib.auth.forms import PasswordChangeForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs[
            'class'] = 'glyphicon glyphicon-envelope form-control-feedback border-radius'
        self.fields['username'].widget.attrs['placeholder'] = 'MAIL:'

        self.fields['password'].widget.attrs[
            'class'] = 'glyphicon glyphicon-envelope form-control-feedback'
        self.fields['password'].widget.attrs['placeholder'] = 'PASS:'
