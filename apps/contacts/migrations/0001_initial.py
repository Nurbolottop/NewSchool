# Generated by Django 4.1.3 on 2022-12-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_site', models.CharField(max_length=255, verbose_name='Телефон номер')),
                ('email_site', models.EmailField(max_length=255, verbose_name='Почта')),
                ('facebook_site', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram_site', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('youtube_site', models.URLField(blank=True, null=True, verbose_name='Youtube')),
            ],
            options={
                'verbose_name': 'Контакттар',
                'verbose_name_plural': 'Контакттар',
            },
        ),
    ]
