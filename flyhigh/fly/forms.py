from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegistrationForm(UserCreationForm):
    password2 = forms.CharField(required=True,label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password*'}))
    password1 = forms.CharField(required=True,label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password*'}))
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Username*'}),
            'email':forms.EmailInput(attrs={'placeholder':'Email*'}),
            'first_name':forms.TextInput(attrs={'placeholder':'First Name*'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last Name*'}),
            'password1':forms.PasswordInput(attrs={'placeholder':'Password*'}),
            'password2':forms.PasswordInput(attrs={'placeholder':'Confirm Password*'}),
            
            }