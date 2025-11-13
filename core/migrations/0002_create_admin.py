from django.db import migrations
from django.contrib.auth.models import User


def create_admin(apps, schema_editor):
    User = apps.get_model("auth", "User")
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin", email="admin@example.com", password="Admin123!"
        )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
