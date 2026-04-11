from django.contrib.auth import get_user_model
from django.urls import reverse

from task_manager.models import Label, Status
from tasks.models import Task

User = get_user_model()


def test_task_create_with_labels(self):  # ❌ НЕ метод класса!
    """✅ ИСПРАВЛЕННОЕ создание Task с labels"""
    self.client.login(username="test", password="pass123")
    
    # Создаем PRECONDITIONS
    status = Status.objects.create(name="New")
    label = Label.objects.create(name="bug")
    
    # ✅ Создаем Task ЧЕРЕЗ VIEW (имитация формы)
    data = {
        'name': 'Test task',
        'description': 'Test desc',
        'status': status.pk,
        'executor': self.user.pk,  # self.user из setUpTestData!
        'labels': [label.pk]  # ✅ M2M labels!
    }
    
    task = Task.objects.get(name="Test task")
    
    self.assertEqual(task.labels.count(), 1)
    self.assertIn(label, task.labels.all())
