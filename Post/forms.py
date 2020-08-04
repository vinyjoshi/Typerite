from django import forms
from .models import Blog, Comment
from .choices import Category_list

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'Title','Author','Category','Photo','Content',
        )
        widgets = {
            'Title' : forms.TextInput(attrs={"class": "form-field full-width"}),
            'Author' : forms.Select(attrs={"class": "form-field full-width"}),
            'Content' : forms.Textarea(attrs={"class": "message form-field full-width"}),
            'Category' : forms.Select(choices=Category_list,attrs={"class": "form-field full-width"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'Name','Comment',
        )
        widgets = {
            'Name' : forms.TextInput(attrs={"class": "form-field full-width"}),
            'Comment' : forms.Textarea(attrs={"class": "message form-field full-width"}),
        }

