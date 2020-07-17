from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib import messages

# Create your views here.
def Post(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        blog : 'blog',
    }
    return render(request, 'Post/detailed.html' , context)


def Category(request):
    return render(request, 'Post/category.html' , {})


def Add(request):
    if request.method == 'POST':
        Title = request.POST['Title']
        Tag = request.POST['Tag']
        Photo = request.POST['Photo']
        Photo1 = request.POST['Photo1']
        Photo2 = request.POST['Photo2']
        Thumbnail = request.POST['Thumbnail']
        Video = request.POST['Video']
        Content = request.POST['Content']

        Blog.objects.create(Title=Title,Tag=Tag,Photo=Photo,Photo1=Photo1,Content=Content,
                            Photo2=Photo2,Thumbnail=Thumbnail,Video=Video).save()
        messages.success(request, 'Your Blog has been Uploaded!')
        return redirect('/')
    else:    
        return render(request, 'Post/add.html', {})