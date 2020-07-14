from django.shortcuts import render

# Create your views here.
def Post(request):
    return render(request, 'Post/detailed.html' , {})

def Add(request):
    return render(request, 'Post/add.html', {})