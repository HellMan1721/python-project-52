from django.contrib.auth import get_user_model

from task_manager.models import Label
from tasks.models import Task

User = get_user_model()


def test_task_create_with_labels(self):  # ❌ НЕ метод класса!
    """✅ ИСПРАВЛЕННОЕ создание Task с labels"""
    self.client.login(username="test", password="pass123")
    
    label = Label.objects.create(name="bug")
    
    task = Task.objects.get(name="Test task")
    
    self.assertEqual(task.labels.count(), 1)
    self.assertIn(label, task.labels.all())
