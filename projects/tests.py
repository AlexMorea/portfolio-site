# projects/tests.py
from django.test import TestCase
from .models import Project


class ProjectModelTest(TestCase):
    def test_str_and_slug_generation(self):
        p = Project.objects.create(
            title="My Test Project", slug="", short_description="x"
        )
        # save triggers slug generation
        self.assertTrue("my-test-project" in p.slug)
        self.assertEqual(str(p), "My Test Project")
