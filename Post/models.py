from django.db import models
from datetime import datetime


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)    
    time = models.TimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title