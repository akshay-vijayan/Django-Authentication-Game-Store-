from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation



class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","style":"background-color:rgba(255,255,255,0.2)"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","style":"background-color:rgba(255,255,255,0.2)"}))

class RegForm(UserCreationForm):
    password1 = forms.CharField(
            label=("password"),
            required=False,
            strip=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control","style":"width:260px;margin-bottom:14px;background-color:rgba(255,255,255,0.2)"}),
            help_text=password_validation.password_validators_help_text_html(),
        )
    password2 = forms.CharField(
            label=("password confirmation"),
            required=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control","style":"width:260px;margin-bottom:40px;background-color:rgba(255,255,255,0.2)"}),
            strip=False,
            help_text=("Enter the same password as before, for verification."),
        )
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control","style":"width:260px;margin-bottom:14px;background-color:rgba(255,255,255,0.2)"}),
            "email":forms.EmailInput(attrs={"class":"form-control","style":"width:260px;margin-bottom:14px;background-color:rgba(255,255,255,0.2)"}),
        }
