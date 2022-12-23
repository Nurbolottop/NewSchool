# Generated by Django 4.1.3 on 2022-12-23 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcreditationList1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Аты')),
            ],
            options={
                'verbose_name': 'Институциялдык аккредитация',
                'verbose_name_plural': 'Институциялдык аккредитация',
            },
        ),
        migrations.CreateModel(
            name='AcreditationList1Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accreditation_detail', models.FileField(upload_to='accreditation/', verbose_name='Документ файл')),
                ('name', models.CharField(max_length=255, verbose_name='Аты')),
                ('accreditation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accreditation', to='inst_akred.acreditationlist1', verbose_name='Аккредитация')),
            ],
            options={
                'verbose_name': 'Институциялдык аккредитация болумго киргизуу',
                'verbose_name_plural': 'Институциялдык аккредитация болумго киргизуу',
            },
        ),
    ]