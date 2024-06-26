# Generated by Django 4.1.5 on 2023-01-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_profession_options_profession_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaryByYear', models.ImageField(upload_to='./static/image')),
                ('vacancyByYear', models.ImageField(upload_to='./static/image')),
                ('salaryByYearForProfession', models.ImageField(upload_to='', verbose_name='./static/image')),
                ('vacancyByYearForProfession', models.ImageField(upload_to='', verbose_name='./static/image')),
            ],
            options={
                'verbose_name': 'Восстребованость',
                'verbose_name_plural': 'Восстребованость',
            },
        ),
        migrations.AlterField(
            model_name='profession',
            name='image',
            field=models.ImageField(upload_to='./static/image'),
        ),
    ]
