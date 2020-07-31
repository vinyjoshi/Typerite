from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import *
from .models import Blog, Comment
from django.views import View
from .forms import BlogForm
from Post.models import *


# Create your views here.
class Post(DetailView):
    model = Blog
    template_name = 'Post/detailed.html'

def CategoryView(request,cats):
    Category_is = Blog.objects.filter(Category=cats)
    Categories = Category.objects.all()
    context = {
        'Category_is':Category_is,
        'cats':cats.title(),
        'Categories' : Categories,
    }
    return render(request, 'Post/category.html', context)    

class Add(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'Post/add.html'

class DeletePOST(DeleteView):
    model = Blog
    template_name = 'Post/Delete.html'
    success_url = reverse_lazy("Home")

class EditPOST(UpdateView):
    model = Blog
    template_name = 'Post/Edit.html'
    fields = ['Title','Tag','Content','Photo','Category']