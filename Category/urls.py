from django.urls import path
from . import views

urlpatterns = [
    path('lifestyle', views.Category, name='Category'),
]