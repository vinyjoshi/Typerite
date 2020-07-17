from django.urls import path
from . import views

urlpatterns = [
    path('Add/', views.Add, name='Add'),
    path('Category/', views.Category, name='Category'),
    path('detail/', views.Post, name='Blog'),
]