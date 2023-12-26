from django.shortcuts import render
from .models import MY_WORK

# Create your views here.

def My_Work(request):
    My_Work_list = MY_WORK.objects.all()
    context = {
        'my_work' : My_Work_list
    }
    return render(request,'My_Work/My_Work.html',context)