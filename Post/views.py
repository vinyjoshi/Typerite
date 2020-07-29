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
    
class Add(View):
    model = Blog
    form_class = BlogForm
    template_name = 'Post/add.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Blog has been Uploaded!')
        return render(request, self.template_name, {'form':form})
    