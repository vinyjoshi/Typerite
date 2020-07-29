from django.urls import path
from .views import Home,About,contact

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('About', About.as_view(), name='About'),    
    path('Contact', contact.as_view(), name='Contact'),    
]   