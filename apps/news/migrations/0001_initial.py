# Generated by Django 4.1.3 on 2022-12-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_news', models.CharField(max_length=255, verbose_name='Название.')),
                ('image_news', models.ImageField(upload_to='news_image/', verbose_name='Фотография')),
                ('description_news', models.TextField(verbose_name='Описание')),
                ('created_news', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
