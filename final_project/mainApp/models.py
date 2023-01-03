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
        return 'Восстребованость'

    class Meta:
        verbose_name = 'Восстребованость'
        verbose_name_plural = 'Восстребованость'
