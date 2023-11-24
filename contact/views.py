from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import UserContactForm
from .forms import ContactForm


def contact(request):
    '''View to return the contact page '''

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            UserContactForm.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            messages.success(request, f'Your query "{subject}" has been submitted successfully')

        return redirect(reverse('home'))

    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data['name'] = request.user.username
            initial_data['email'] = request.user.email
        form = ContactForm(initial=initial_data)

    return render(request, 'contact/contact.html', {'form': form})