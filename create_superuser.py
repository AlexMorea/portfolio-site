import os
from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = os.environ.get("DJANGO_SUPERUSER_USERNAME")
EMAIL = os.environ.get("DJANGO_SUPERUSER_EMAIL")
PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if USERNAME and EMAIL and PASSWORD:
    if not User.objects.filter(username=USERNAME).exists():
        User.objects.create_superuser(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD
        )
        print("Superuser created successfully!")
    else:
        print("Superuser already exists.")
        