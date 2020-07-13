from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Add', views.Add, name='Add'),
    path('Post', views.Post, name='DetailView'),    
    path('About', views.About, name='About'),    
    path('Contact', views.Contact, name='Contact'),    
]   