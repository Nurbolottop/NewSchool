from django.db import models

# Create your models here.
class Parents(models.Model):
    name = models.CharField(max_length=244, verbose_name='Суроо!')
    desc = models.TextField(verbose_name='Жоор!')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ата энелерге!"
        verbose_name_plural = "Ата эненлерге"