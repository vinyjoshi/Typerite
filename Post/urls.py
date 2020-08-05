from django.urls import path
from .views import *

urlpatterns = [
    path('Add/', Add.as_view(), name='Add'),
    path('Detail/Edit/<int:pk>/', EditPOST.as_view(), name='Edit'),
    path('Detail/<int:pk>/Delete/', DeletePOST.as_view(), name='Delete'),
    path('Detail/<int:pk>/', Post.as_view(), name='Blog'),
    path('Category/<str:cats>/', CategoryView, name='Category'),
    path('Detail/<int:pk>/Comment', PostComment, name='PostComment'),
]