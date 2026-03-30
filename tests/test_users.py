from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            password='12345'
        )

    def test_user_list(self):
        response = self.client.get(reverse('users:users'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_user_create(self):
        self.client.post(reverse('users:user_create'), {
            'first_name': 'New',
            'last_name': 'User', 
            'username': 'newuser',
            'password': 'password123'
        })
        self.assertEqual(User.objects.count(), 2)
