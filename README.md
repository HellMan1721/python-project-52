# Task Manager (Python/Django)

[![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=HellMan1721_python-project-52&metric=coverage)](https://sonarcloud.io/dashboard?id=HellMan1721_python-project-52)

[![Actions Status](https://github.com/HellMan1721/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/HellMan1721/python-project-52/actions)

Веб-приложение для управления задачами с пользователями, статусами, метками и фильтрами.

## ✨ Функции
- Регистрация/авторизация
- CRUD: Users, Statuses, Labels, Tasks
- Фильтры задач (author, status, executor, labels)
- Права доступа (только владелец редактирует)
- Bootstrap UI
- Rollbar мониторинг ошибок

## 🛠 Установка

```bash
git clone https://github.com/твой_username/python-project-52.git
cd python-project-52
make install
# Заполни .env (SECRET_KEY, DATABASE_URL)
make migrate
make dev-start
```

**Доступ**: http://localhost:8000

## 🧪 Тестирование

```bash
make test  # Тесты
make test-coverage  # Покрытие тестами
```

## 🚀 Деплой

**Render**:

```bash
Build: make install && make collectstatic
Start: uv run gunicorn task_manager.wsgi:application
```
