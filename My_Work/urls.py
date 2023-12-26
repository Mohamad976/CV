from django.urls import path
from . import views


app_name = 'My_Work'

urlpatterns = [
    path('portfolio/',views.My_Work,name='My_Work_list')
]