from django.contrib import admin
from mainApp.models import Profession, Demand, SalaryByCities, VacancyByCities, StatisticsByYear, Skills, GeographyGraphics, SkillsGraphics

admin.site.register(Profession)
admin.site.register(Demand)
admin.site.register(SalaryByCities)
admin.site.register(VacancyByCities)
admin.site.register(StatisticsByYear)
admin.site.register(Skills)

admin.site.register(GeographyGraphics)
admin.site.register(SkillsGraphics)
admin.site.register(SalaryByCitiesNeeded)
admin.site.register(VacancyByCitiesNeeded)
