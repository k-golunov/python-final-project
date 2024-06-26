from django.shortcuts import render

from mainApp import GetApiData
from mainApp.models import Profession, Demand, SalaryByCities, VacancyByCities, StatisticsByYear, Skills, \
    GeographyGraphics, SkillsGraphics, VacancyByCitiesNeeded, SalaryByCitiesNeeded


# Create your views here.

def index_page(request):
    data = {
        'profession': Profession.objects.get(id=1)
    }
    return render(request, 'index.html', context=data)


def demand_page(request):
    data = {
        'demand': Demand.objects.get(id=2),
        'statistic': StatisticsByYear.objects.all(),
    }
    return render(request, 'demand.html', context=data)


def geography_page(request):
    data = {
        'salaryByCities': SalaryByCities.objects.all(),
        'vacancyByCities': VacancyByCities.objects.all(),
        'vacancyByCitiesNeeded': VacancyByCitiesNeeded.objects.all(),
        'salaryByCitiesNeeded': SalaryByCitiesNeeded.objects.all(),
        'graphics': GeographyGraphics.objects.get(id=1),
    }
    return render(request, 'geography.html', context=data)


def skills_page(request):
    data = {
        'skills': Skills.objects.all(),
        'graphics': SkillsGraphics.objects.get(id=1),
    }
    return render(request, 'skills.html', context=data)


def api_page(request):
    data = {
        'vacancy': GetApiData.GetData()
    }
    return render(request, 'api.html', context=data)
