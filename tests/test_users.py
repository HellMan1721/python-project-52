from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class UserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", first_name="Test", 
            last_name="User", password="12345"
        )
        cls.admin = User.objects.create_superuser(
            username="admin", password="admin123"
        )

    def test_user_list_authenticated(self):  # ✅ Login!
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("users:users"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")

    def test_user_create_authenticated(self):
        self.client.login(username="admin", password="admin123")  # ✅ Admin!
        self.client.post(reverse("users:create"), {
            "first_name": "New", "last_name": "User",
            "username": "newuser", "password1": "pass123", 
            "password2": "pass123"
        })
        self.assertEqual(User.objects.count(), 3)
