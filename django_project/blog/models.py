from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # auto_now = True ya da auto_now_add true yapabilirdik ancak onlari degistiremiyoruz istedigimizde tarihi degistirebilmek icin timezone kullandik ve now() fonksiyonunuu calistirmadik sadece cagirdik
    author = models.ForeignKey(User, on_delete=models.CASCADE) #eger user silinirse onun yazdigi tum postlar da silinsin

    def __str__(self):
        return self.title