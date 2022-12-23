# Generated by Django 4.1.3 on 2022-12-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_student', models.CharField(max_length=255, verbose_name='Мугалимдин аты.')),
                ('image_student', models.ImageField(upload_to='student_image/', verbose_name='Мугалимдин суроту')),
                ('description_student', models.TextField(verbose_name='Мугалимдин кызматы.')),
            ],
            options={
                'verbose_name': 'Мугалимдер',
            },
        ),
    ]
