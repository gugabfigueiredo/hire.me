from django.db import models


# Create your models here.
class Urls(models.Model):

    alias = models.SlugField(max_length=6, primary_key=True)
    httpurl = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
    favicon = models.ImageField(default='null.png', upload_to='favicons')

    def __str__(self):
        return self.httpurl