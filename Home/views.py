from django.shortcuts import render, redirect
from .models import *
from Post.models import *
from django.contrib import messages
from django.views import View 
from django.views.generic import ListView
from .forms import ContactForm

# Create your views here.
class Home(ListView):
    model = Blog
    template_name = 'Home/Index.html'

    def get_context_data(self,*args,**kwargs):
        Categories = Category.objects.all()
        context = super(Home,self).get_context_data(*args,**kwargs)
        context["Categories"] = Categories
        return context

class About(View):
    template_name = 'Home/about.html'

    def get(self,request):
        Categories = Category.objects.all()
        return render(request, self.template_name, {'Categories':Categories})

class contact(View):
    form_class = ContactForm
    template_name = 'Home/contact.html'

    def get(self, request):
        Categories = Category.objects.all()
        form = self.form_class()
        return render(request,self.template_name, {'Categories':Categories,'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Message has been delivered to our people. We will get back to you ASAP!')
            return redirect('Home')
    
 