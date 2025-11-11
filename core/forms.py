# core/forms.py
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Your name", "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "you@example.com", "class": "form-control"}
            ),
            "subject": forms.TextInput(
                attrs={"placeholder": "Subject (optional)", "class": "form-control"}
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Write your message...",
                    "class": "form-control",
                    "rows": 6,
                }
            ),
        }
