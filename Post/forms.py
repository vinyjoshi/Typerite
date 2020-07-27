from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'Title','Tag','Photo','Photo1','Photo2','Thumbnail','Video','Content',
        ]