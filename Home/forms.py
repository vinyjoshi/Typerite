from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'Name', 'Email', 'Message'            
        )
        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-field full-width'}),
            'Email' : forms.TextInput(attrs={'class':'full-width'}),
            'Message' : forms.Textarea   (attrs={'class':'message full-width'}),
        }