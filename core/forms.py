from django import forms
from django.core.validators import EmailValidator
from .models import Contact
import bleach

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            # Remove any HTML tags and limit length
            name = bleach.clean(name, strip=True)
            if len(name) < 2:
                raise forms.ValidationError("Name is too short")
            if len(name) > 100:
                raise forms.ValidationError("Name is too long")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Validate email format
            validator = EmailValidator()
            validator(email)
            email = email.lower().strip()
        return email

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if subject:
            # Remove any HTML tags and limit length
            subject = bleach.clean(subject, strip=True)
            if len(subject) < 3:
                raise forms.ValidationError("Subject is too short")
            if len(subject) > 200:
                raise forms.ValidationError("Subject is too long")
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            # Remove any dangerous HTML tags but allow basic formatting
            allowed_tags = ['p', 'br']
            message = bleach.clean(message, tags=allowed_tags, strip=True)
            if len(message) < 10:
                raise forms.ValidationError("Message is too short")
            if len(message) > 5000:
                raise forms.ValidationError("Message is too long")
        return message
