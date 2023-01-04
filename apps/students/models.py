from django.db import models

# Create your models here.
class Studet(models.Model):
    name_student = models.CharField(
        max_length=255,
        verbose_name='Класстын аты.'
    )
<<<<<<< HEAD
=======

   
>>>>>>> 4ed2c14ad15feaf4f31c61eb3fb9132f77e518f3
    image_student = models.ImageField(
        upload_to='student_image/',
        verbose_name='Класстын суроту'
    )

    def __str__(self):
        return self.name_student

    class Meta:
        verbose_name = "Класстар"
        verbose_name = "Класстар"
        ordering = ('id', )