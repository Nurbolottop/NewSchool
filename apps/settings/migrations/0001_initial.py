# Generated by Django 4.1.3 on 2022-11-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_site', models.CharField(max_length=244, verbose_name='Название сайта!')),
                ('logo_site', models.ImageField(upload_to='logo_site/', verbose_name='Логотип сайта')),
                ('description_site', models.TextField(verbose_name='Описание сайта')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
