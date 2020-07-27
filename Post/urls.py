from django.urls import path
from .views import Add, Post

urlpatterns = [
    path('Add/', Add.as_view(), name='Add'),
    path('detail/', Post, name='Blog'),
    path('Add/', views.Add, name='Add'),
    path('Category/', views.Category, name='Category'),
    path('detail/<int:pk>', views.Post, name='Blog'),
]