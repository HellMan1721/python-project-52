from django import forms
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    widgets = {
        'labels': forms.CheckboxSelectMultiple(),
    }
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Задача успешно создана')
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    widgets = {
        'labels': forms.CheckboxSelectMultiple(),
    }
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:tasks')


    def get(self, request, *args, **kwargs):
        task = self.get_object()

        if task.author != request.user:
            messages.error(
                request,
                'Задачу может редактировать только её автор'
            )
            return redirect('tasks:tasks')

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        task = self.get_object()

        if task.author != request.user:
            messages.error(
                request,
                'Задачу может редактировать только её автор'
            )
            return redirect('tasks:tasks')

        messages.success(request, 'Задача успешно изменена')
        return super().post(request, *args, **kwargs)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:tasks')

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != request.user:
            messages.error(
                request,
                'Задачу может удалить только её автор'
            )
            return redirect('tasks:tasks')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != request.user:
            messages.error(
                request,
                'Задачу может удалить только её автор'
            )
            return redirect('tasks:tasks')
        messages.success(request, 'Задача успешно удалена')
        return super().post(request, *args, **kwargs)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/show.html'
    context_object_name = 'task'