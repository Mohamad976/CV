from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolios' : portfolio_list
    }
    return render(request,'portfolio/portfolio.html',context)