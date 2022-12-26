from django.contrib import admin

from apps.achyk.models import AchykSaat, AchykSaatDetail

# Register your models here.
admin.site.registe(AchykSaatDetail)
admin.site.registe(AchykSaat)
