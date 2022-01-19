from django.db import models
from tinymce.models import HTMLField
# Create your models here.



class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_subtitle = models.TextField()
    news_date = models.DateTimeField(auto_now_add=True)
    news_text = HTMLField()
    image = models.ImageField(default="default.jpg", upload_to='uploads/')

    def __str__(self):
        return self.news_title

    @property
    def news_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Dealers(models.Model):
    region = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    working_days = HTMLField(default="24/7")

    def __str__(self):
        return self.name


class TextsToTranslate(models.Model):
    title = models.CharField(max_length=200)
    text_uz = HTMLField()
    text_ru = HTMLField()
    text_en = HTMLField()


    def __str__(self):
        return self.title