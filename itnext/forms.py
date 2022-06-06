from django import forms
from django.contrib.auth.models import User
from django.forms import EmailInput, PasswordInput, TextInput, ModelForm
from .models import Email, PostComment
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


class PostCommentForm(ModelForm):
    class Meta:
        model = PostComment
        fields = '__all__'

        widgets = {
            'email': EmailInput(attrs={
                'class':'field_custom',
                'placeholder':'Email'}),
            'phone': TextInput(attrs={
                'class': 'field_custom',
                'placeholder': 'Phone'}),
            'password': PasswordInput(attrs={
                'class': 'field_custom',
                'placeholder': 'Password'}),
            'comment': TextInput(attrs={
                'class': 'field_custom',
                'placeholder': 'Comment'})
        }