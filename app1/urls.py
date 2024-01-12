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
    path('feature/', views.feature, name="feature"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.userLogout, name="logout"),
    path('profile/', views.profile, name="profile"),

]
