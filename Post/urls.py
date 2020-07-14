from django.urls import path
from . import views

urlpatterns = [
    path('Add/', views.Add, name='Add'),
    path('detail/', views.Post, name='Blog'),
]