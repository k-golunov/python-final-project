from django.db import models


# Create your models here.
class Profession(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    # image = models.ImageField('Картинка')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
