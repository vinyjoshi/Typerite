from django.db import models
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('/')

class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Tag = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)    
    time = models.TimeField(auto_now_add=True)
    Content = RichTextField(blank=False, null=True)
    Photo = models.ImageField(null=True,blank=True,upload_to='photos/%Y/%m/%d/')
    Category = models.CharField(max_length=255,default='Nature')
    
    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse('Home')

class Comment(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Comment = models.TextField(blank=False)
    
    def __str__(self):
       return self.Name