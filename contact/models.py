from django.db import models
from django.contrib.auth.models import User


class UserContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150, null=True,
                               blank=True,
                               default="AEH Art Enquiry")
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
