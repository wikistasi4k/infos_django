from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('me/', views.about_me, name='about_me'),
    path('contact/', views.contact, name='contact'),
]