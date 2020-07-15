from django.db import models
from datetime import datetime


# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Tag = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)    
    time = models.TimeField(auto_now_add=True)
    Content = models.TextField(blank=False)
    Photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    Photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.Title

class Comment(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Comment = models.TextField(blank=False)
    
    def __str__(self):
       return self.Name