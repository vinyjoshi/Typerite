from django.shortcuts import render, redirect
from .models import *
from Post.models import Blog
from django.contrib import messages

# Create your views here.
def Home(request):
    Blogs = Blog.objects.all().order_by('-date')
    for i in range(s):
        if (Blogs[i]):
            print(Blogs[i].Title)
            #data = (Blog.objects.get(pk=i).Content).split("\n",2)
            #print(i)
    context = {
        Blogs : 'Blogs'
    }
    return render(request, 'Home/Index.html', context)

def About(request):
    return render(request, 'Home/about.html', {})

def contact(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Message = request.POST['Message']
        
        Contact.objects.create(Name=Name,Email=Email,Message=Message).save()
        messages.success(request, 'Your Message has been delivered to our people. We will get back to you ASAP!')
        return redirect('/')
    else:
        return render(request, 'Home/contact.html', {})