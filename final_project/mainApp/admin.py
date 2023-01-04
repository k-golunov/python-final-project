from django.contrib import admin
from mainApp.models import Profession, Demand, SalaryByCities, VacancyByCities, StatisticsByYear

admin.site.register(Profession)
admin.site.register(Demand)
admin.site.register(SalaryByCities)
admin.site.register(VacancyByCities)
admin.site.register(StatisticsByYear)