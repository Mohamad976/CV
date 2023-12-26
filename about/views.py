from django.shortcuts import render
from .models import About
from .models import Service
from .models import Skill


# Create your views here.

def about(request):
    about_list = About.objects.all()
    service_list = Service.objects.all()
    skill_list = Skill.objects.all()

    context = {
        'abouts' : about_list,
        'services' : service_list,
        'skills' : skill_list
    }
    return render(request,'about/about.html',context)