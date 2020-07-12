from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Home/Index.html', {})

def About(request):
    return render(request, 'Home/about.html', {})

def Contact(request):
    return render(request, 'Home/contact.html', {})

def Post(request):
    context = {}
    return render(request, 'Home/detailed.html', context)