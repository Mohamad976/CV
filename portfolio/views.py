from django.shortcuts import render
from .models import Portfolio, Work

# Create your views here.

def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolios' : portfolio_list
    }
    return render(request,'portfolio/portfolio.html',context)


def work(request,id):
    work = Portfolio.objects.get(id=id)
    work_details = Work.objects.all().filter(portfolio = work)
    context = {
        'work' : work,
        'work_details' : work_details

    }
    return render(request,'portfolio/work.html',context)
