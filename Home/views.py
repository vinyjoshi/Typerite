from django.shortcuts import render, redirect
from .models import *
from Post.models import Blog
from django.contrib import messages

# Create your views here.
def Home(request):
<<<<<<< HEAD
    Blogs = Blog.objects.all().order_by('-date')
=======
    Post = Blog.objects.all().order_by('-date')
>>>>>>> 2f781aee9cc7c95e0e1eaf8712c07add387d0677
    #for i in range(s):
    #    if (Blogs[i]):
    #        print(Blogs[i].Title)
            #data = (Blog.objects.get(pk=i).Content).split("\n",2)
            #print(i)
    context = {
        Post : 'Post',
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
        return redirect('Home')
    else:
        return render(request, 'Home/contact.html', {})