from django.shortcuts import render

from mainApp.models import Profession, Demand, SalaryByCities, VacancyByCities, StatisticsByYear, Skills


# Create your views here.

def index_page(request):
    data = {
        'profession': Profession.objects.get(id=1)
    }
    return render(request, 'index.html', context=data)


def demand_page(request):
    data = {
        'demand': Demand.objects.get(id=1),
        'statistic': StatisticsByYear.objects.all(),
    }
    return render(request, 'demand.html', context=data)


def geography_page(request):
    data = {
        'salaryByCities': SalaryByCities.objects.all(),
        'vacancyByCities': VacancyByCities.objects.all(),
    }
    return render(request, 'geography.html', context=data)


def skills_page(request):
    data = {
        'skills': Skills.objects.all()
    }
    return render(request, 'skills.html', context=data)
