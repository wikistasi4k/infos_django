
from django.shortcuts import render

def home(request):
    return render(request, 'infos/home.html')

def about_me(request):
    return render(request, 'infos/about_me.html')

def contact(request):
    return render(request, 'infos/contact.html')

