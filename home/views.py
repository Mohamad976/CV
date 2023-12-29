from django.shortcuts import render
from .models import Home

# Create your views here.

def home(request):
    home_list = Home.objects.all()
    context = {
        'homes' : home_list
    }
    return render(request,'home/home.html',context)