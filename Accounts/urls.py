from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.Login, name='Login'),
    path('Register', views.Register, name='Register'),    
    path('Timeline', views.Timeline, name='Timeline'),    
]   