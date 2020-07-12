from django.shortcuts import render
from .models import Blog

# Create your views here.
def Category(request):
    post = Blog.objects.all()
    #if(tag__icontains='Lifestyle'):
    #   context = {}
    #if(tag__icontains='Family'):
    #   context = {}
    #if(tag__icontains='Health'):
    #   context = {}
    #if(tag__icontains='Management'):
    #   context = {}
    #if(tag__icontains='Travel'):
    #  context = {}
    #if(tag__icontains='Work'):
    #   context = {}
    return render(request, 'Category/idk.html', {})
