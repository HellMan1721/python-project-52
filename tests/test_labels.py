from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from task_manager.models import Label, Status
from tasks.models import Task


User = get_user_model()


class LabelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.status = Status.objects.create(name="Test Status")
        cls.user = User.objects.create_user(username="test", password="pass123")
    
    def setUp(self):
        # ❌ УБЕРИ self.client = Client() - создается автоматически!
        self.label = Label.objects.create(name="bug")

    def test_cannot_delete_if_used(self):
        """✅ Реальный тест запрета удаления"""
        task = Task.objects.create(
            name="test task", author=self.user, 
            status=self.status, executor=self.user
        )
        task.labels.add(self.label)
        
        self.client.login(username="test", password="pass123")
        
        # ✅ ПОПЫТКА удаления через VIEW
        response = self.client.post(reverse("labels:delete", kwargs={"pk": self.label.pk}))
        
        # ✅ Label НЕ удален!
        self.assertTrue(Label.objects.filter(name="bug").exists())
        self.assertEqual(response.status_code, 302)  # Редирект с ошибкой
        
    def test_label_str(self):  # ✅ +Coverage models.py
        """Покрытие __str__"""
        self.assertEqual(str(self.label), "bug")