from django import forms
from .models import UserContactForm

# Create the form class
class ContactForm(forms.ModelForm):
    class Meta:
        model = UserContactForm
        fields = ['name', 'email', 'subject', 'message',]
