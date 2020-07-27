from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.contrib import messages
from django.views import View
from .forms import BlogForm

# Create your views here.
def Post(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        blog : 'blog',
    }
    return render(request, 'Post/detailed.html' , context)


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
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})
    