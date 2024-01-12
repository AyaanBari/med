from django.shortcuts import render

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
