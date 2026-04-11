from django.urls import reverse, resolve
from django.test import TestCase


class TestTaskURLs(TestCase):
    def test_urls_resolve(self):
        """✅ 100% coverage всех urls.py"""
        urls = [
            reverse('tasks:tasks'),
            reverse('tasks:create'), 
            reverse('tasks:update', kwargs={'pk': 1}),
            reverse('tasks:delete', kwargs={'pk': 1}),
        ]
        for url in urls:
            resolver = resolve(url)
            self.assertIn('tasks', resolver.app_names)
