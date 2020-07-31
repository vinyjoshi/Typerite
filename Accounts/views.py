from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from Post.models import *
from Home.models import *
from django.views.generic import *

# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are now logged in')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials! Try Again.')
            return redirect('Login')
    else:
        return render(request, 'Accounts/login.html')

def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'Logout Successfull')
        return redirect('/')

def Register(request):
    if request.method == 'POST':
        # Get form values:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        # Check if password matches:
        if password == password2:
            # Check if username already exist:
            if User.objects.filter(username='username').exists():
                messages.error(request, 'Username already taken!')
                return redirect('Register')
            else:
                # Check email:
                if User.objects.filter(email='email').exists():
                    messages.error(request, 'Email already registered for other user!')
                    return redirect('Register')
                else:
                    User.objects.create_user(username=username,email=email,first_name=first_name,
                                            last_name=last_name,password=password).save()
                    messages.success(request, 'Registered Successfully!')
                    return redirect('Login')
                    # auth.login(request, user) from djanngo.contrib import auth ==> To login directly               
        else:
            messages.error(request, 'The Passwords donot match!')
            return redirect('Register')
    else:
        return render(request, 'Accounts/register.html')

class Timeline(View):
    model = Blog
    template_name = 'Accounts/timeline.html'

    def get(self,request):
        timeline = Blog.objects.all().filter(Author_id=request.user.id)
        context = {
            "timeline":timeline,
        }
        return render(request,self.template_name,context)
        