from django.urls import path
from .views import Add, Post

urlpatterns = [
    path('Add/', Add.as_view(), name='Add'),
    path('detail/', Post, name='Blog'),
]