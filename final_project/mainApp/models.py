from django.db import models


# Create your models here.
class Profession(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='./static/image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Demand(models.Model):
    salaryByYear = models.ImageField('График зп по годам',upload_to='./static/image')
    vacancyByYear = models.ImageField(upload_to='./static/image')
    salaryByYearForProfession = models.ImageField(upload_to='./static/image')
    vacancyByYearForProfession = models.ImageField(upload_to='./static/image')

    def __str__(self):
        return 'Графики'

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'


class SalaryByCities(models.Model):
    city = models.TextField('Город')
    salary = models.TextField('Уровень зарплат')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'География'
        verbose_name_plural = 'Города и их зп'

class VacancyByCities(models.Model):
    city = models.TextField('Город')
    vacancy = models.TextField('Доля вакансий')


    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'География'
        verbose_name_plural = 'Города и доля вакансий'