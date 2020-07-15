from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request, 'Home/Index.html', {})

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