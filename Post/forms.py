from django import forms
from .models import Blog, Comment
from .choices import Category_list

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'Title','Tag','Category','Photo','Photo1','Photo2','Thumbnail','Video','Content',
        )
        widgets = {
            'Title' : forms.TextInput(attrs={"class": "form-field full-width"}),
            'Tag' : forms.TextInput(attrs={"class": "form-field full-width"}),
            'Content' : forms.Textarea(attrs={"class": "message form-field full-width"}),
            'Category' : forms.Select(choices=Category_list,attrs={"class": "form-field full-width"}),
            
        }

