from django.shortcuts import render

from mainApp.models import Profession, Demand


# Create your views here.

def index_page(request):
    data = {
        'profession': Profession.objects.get(id=1)
    }
    return render(request, 'index.html', context=data)


def demand_page(request):
    data = {
        'demand': Demand.objects.get(id=1)
    }
    return render(request, 'demand.html', context=data)
