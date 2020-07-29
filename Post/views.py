from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from django.contrib import messages
from django.views import View
from django.views.generic import *
from .forms import BlogForm

# Create your views here.
class Post(DetailView):
    model = Blog
    template_name = 'Post/detailed.html'

def CategoryView(request,cats):
    Category_is = Blog.objects.filter(Category=cats)
    context = {
        'Category_is':Category_is,
        'cats':cats.title(),
    }
    return render(request, 'Post/category.html', context)    

class Add(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'Post/add.html'

    