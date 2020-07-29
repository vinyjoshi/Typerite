from django.urls import path
from .views import Add, Post, CategoryView

urlpatterns = [
    path('Add/', Add.as_view(), name='Add'),
    path('Detail/<int:pk>/', Post.as_view(), name='Blog'),
    path('Category/<str:cats>/', CategoryView, name='Category'),
]