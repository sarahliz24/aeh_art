from django import forms
from .models import UserContactForm


class ContactForm(forms.ModelForm):
    ''' Create contact form '''
    class Meta:
        model = UserContactForm
        fields = ['name', 'email', 'subject', 'message', ]
