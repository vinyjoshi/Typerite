from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request, 'Accounts/login.html' , {})

def Register(request):
    return render(request, 'Accounts/register.html' , {})

def Timeline(request):
    return render(request, 'Accounts/timeline.html' , {})