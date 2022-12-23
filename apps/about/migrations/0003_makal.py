# Generated by Django 4.1.3 on 2022-12-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_lessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Макал')),
                ('description', models.CharField(max_length=255, verbose_name='Макалдын автору')),
            ],
            options={
                'verbose_name': 'Макалдар',
                'verbose_name_plural': 'Макалдар',
            },
        ),
    ]
