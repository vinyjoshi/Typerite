from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    date = models.CharField(max_length=200)    
    time = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    
    def __str__(self):
        return self.title