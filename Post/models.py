from django.db import models
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('/')

class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)    
    time = models.TimeField(auto_now_add=True)
    Content = RichTextField(blank=False, null=True)
    Photo = models.ImageField(null=True,blank=True,upload_to='photos/%Y/%m/%d/')
    Category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse('Home')

class Comment(models.Model):
    Post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Date = models.DateField(auto_now_add=True)
    Comment = models.TextField(blank=False)
   
    def __str__(self):
       return '%s - %s' % (self.Post.Title, self.Name)
    
class Reply(models.Model):
    Comment = models.ForeignKey(Comment,related_name='replies' ,on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Reply = models.TextField(blank=False)
    Date = models.DateField(auto_now_add=True)

    def __str__(self):
       return '%s - %s' % (self.Comment.Name, self.Name)