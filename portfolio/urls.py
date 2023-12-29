from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('',views.portfolio,name='portfolio_list'),
    path('<int:id>',views.work,name='work')
]