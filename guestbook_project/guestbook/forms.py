from django import forms
from .models import GuestbookEntry

class GuestbookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['author_name', 'author_email', 'entry_text']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'author_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
            'entry_text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст записи'}),
        }
        labels = {
            'author_name': 'Имя',
            'author_email': 'Email',
            'entry_text': 'Текст записи',
        }
