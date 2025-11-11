# core/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage


class ContactTest(TestCase):
    def test_contact_form_saves(self):
        data = {
            "name": "Thabi",
            "email": "thabi@example.com",
            "subject": "Hello",
            "message": "Test message",
        }
        response = self.client.post(reverse("contact"), data)
        # after success should redirect to same page
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            ContactMessage.objects.filter(email="thabi@example.com").exists()
        )


class HomeViewTest(TestCase):
    def test_home_status(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hi, I'm")
