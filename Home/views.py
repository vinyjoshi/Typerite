from django.shortcuts import render, redirect
from .models import *
from Post.models import Blog
from django.contrib import messages
from django.views import View 
from django.views.generic import ListView
from .forms import ContactForm

# Create your views here.
class Home(ListView):
    model = Blog
    template_name = 'Home/Index.html'

class About(View):
    template_name = 'Home/about.html'

    def get(self,request):
        return render(request, self.template_name, {})

class contact(View):
    form_class = ContactForm
    template_name = 'Home/contact.html'

    def get(self, request):
        form = self.form_class()
        return render(request,self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Message has been delivered to our people. We will get back to you ASAP!')
            return redirect('Home')
    
 