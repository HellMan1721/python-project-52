from django.test import TestCase
from django.urls import reverse

class TestAllURLs(TestCase):
    def test_label_urls(self):
        """100% coverage labels/urls.py"""
        self.assertEqual(reverse("labels:list"), "/labels/")
        self.assertEqual(reverse("labels:create"), "/labels/create/")
        
    def test_status_urls(self):
        self.assertEqual(reverse("statuses:statuses"), "/statuses/")
        self.assertEqual(reverse("statuses:create"), "/statuses/create/")
