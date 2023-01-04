from django.contrib import admin
from mainApp.models import Profession, Demand, SalaryByCities, VacancyByCities

admin.site.register(Profession)
admin.site.register(Demand)
admin.site.register(SalaryByCities)
admin.site.register(VacancyByCities)