# Generated by Django 4.1.3 on 2022-12-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Сабакты аты')),
                ('number', models.CharField(max_length=255, verbose_name='Сабактын жакшы отулгон пайызы')),
            ],
            options={
                'verbose_name': 'Биздин сабак',
                'verbose_name_plural': 'Биздин сабактар',
            },
        ),
    ]