from django.urls import path
from .views import *

urlpatterns = [
    path('Login/', Login, name='Login'),
    path('Logout/', Logout, name='Logout'),
    path('Register/', Register, name='Register'),    
    path('Timeline/', Timeline.as_view(), name='Timeline'),    
    path('Edit_profile/', Profile.as_view(), name='Edit_Profile'), 
]   