from .models import *
from django.forms import EmailInput, ModelForm, NumberInput, TextInput, DateTimeInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import AbstractUser

class CreateUserForm(UserCreationForm):
    email=forms.EmailField()
    
    
   
    class Meta:
        model= CustomUser
        fields= ['username',  'email', 'password1', 'password2']

        

class ContactForm(forms.Form):
    subject=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',"rows": 5}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class SendForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    
    
