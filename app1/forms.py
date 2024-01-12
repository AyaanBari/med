from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Pataient    


class PatientForm(UserCreationForm):
    username = forms.CharField(
        label=("User name"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter user name'})
    )
    first_name = forms.CharField(
        label=("First name"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter first name'})
    )
    last_name = forms.CharField(
        label=("Last name"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter last name'})
    )
    mobile = forms.CharField(
        label=("Contact number"),
        widget=forms.NumberInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter Contact number'})
    )
    email = forms.EmailField(
        label=("Email"),
        widget=forms.EmailInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter email'})
    )
    gender = forms.CharField(
        label=("Select Gender"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'placeholder':'Select Gender'}))
    age = forms.CharField(
        label=("Age"),
        widget=forms.NumberInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter age'})
    )    
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter password'})
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter password confirmation'})
    )
    class Meta:
        model = Pataient
        fields = ("username","first_name", "last_name","email", "mobile","gender","age")
    
class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label=("User name"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter user name'})
    )
    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'placeholder':'Enter password'})
    )