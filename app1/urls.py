from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('team/', views.team, name="team"),
    path('appointment/', views.appointment, name="appointment"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('404/', views.error_404, name="404"),
    path('feature/', views.feature, name="feature"),


]
