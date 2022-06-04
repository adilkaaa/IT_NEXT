from django import forms
from django.contrib.auth.models import User
from django.forms import EmailInput, PasswordInput, TextInput
from .models import Email
from django.contrib.auth.forms import UserCreationForm



class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']
        widgets = {
            'email': EmailInput(attrs={
                'name': 'email',
                'class': 'field',
                'placeholder': 'Email'
            })
        }
