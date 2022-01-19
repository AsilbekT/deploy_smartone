from django.contrib import admin
from .models import News, TextsToTranslate, Dealers

# Register your models here.
admin.site.register(News)
admin.site.register(TextsToTranslate)
admin.site.register(Dealers)
