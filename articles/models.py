from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import *
from Apis.models import *

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'articles/', blank=True)
    post = models.CharField('article',max_length=255)
    published_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)    

    def __str__(self):
        return self.title