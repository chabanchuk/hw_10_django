from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    
class RegisterForm(forms.ModelForm):
    Username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())
    password1 = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.TextInput())
    password2 = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.TextInput())
    class Meta:
        model = User
        fields = ['Username', 'password1', 'password2']
