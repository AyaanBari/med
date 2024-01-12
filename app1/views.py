from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . forms import PatientForm,SignInForm
from django.contrib import messages

# Create your views here.   
def home(request):
    return render(request, 'app1/index.html')

def about(request):
    return render(request, 'app1/about.html')

def contact(request):
    return render(request, 'app1/contact.html')

def services(request):
    return render(request, 'app1/service.html')

def team(request):
    return render(request, 'app1/team.html')

def appointment(request):
    return render(request, 'app1/appointment.html')

def testimonial(request):
    return render(request, 'app1/testimonial.html')
def feature(request):
    return render(request, 'app1/feature.html')

def signup(request):
    form=PatientForm()
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Account created successfully')
            except Exception as e:
                messages.error(request, 'Account creation failed')
    else:
        form=PatientForm()
    return render(request, 'app1/signup.html', {'form':form})

def signin(request):
    if request.POST:
        frm=SignInForm(request=request, data=request.POST)
        if frm.is_valid():
            uname=frm.cleaned_data['username']
            upass=frm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/profile/')
    else:
        frm=SignInForm()
    return render(request, 'app1/signin.html', {'form':frm})

def userLogout(request):
    logout(request)
    return redirect('/signin/')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'app1/profile.html')
    else:
        return redirect('/signin/')
