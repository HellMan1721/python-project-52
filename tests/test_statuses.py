from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Status


class StatusTestCase(TestCase):
    @classmethod  
    def setUpTestData(cls):  # ✅ Classmethod!
        cls.user = User.objects.create_user(username="test", password="test")
        cls.status = Status.objects.create(name="Test")  # ✅ Coverage!

    def test_status_create(self):
        self.client.login(username="test", password="test")
        response = self.client.post(
            reverse("statuses:create"),
            {"name": "Новый"}
            )
        self.assertRedirects(response, reverse("statuses:statuses"))
        self.assertEqual(Status.objects.count(), 2)  # + новый статус

    def test_status_str(self):  # ✅ +Coverage
        self.assertEqual(str(self.status), "Test")