from django import forms
from .models import ContactForm


class Contact(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = [
            'name',
            'email',
            'phone',
            'title',
            'description',
            'contact_method'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            'contact_method': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
