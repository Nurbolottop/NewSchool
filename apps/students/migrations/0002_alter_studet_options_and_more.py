# Generated by Django 4.1.3 on 2022-12-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studet',
            options={'verbose_name': 'Класстар'},
        ),
        migrations.RemoveField(
            model_name='studet',
            name='description_student',
        ),
        migrations.AlterField(
            model_name='studet',
            name='image_student',
            field=models.ImageField(upload_to='student_image/', verbose_name='Класстын суроту'),
        ),
        migrations.AlterField(
            model_name='studet',
            name='name_student',
            field=models.CharField(max_length=255, verbose_name='Класстын аты.'),
        ),
    ]
