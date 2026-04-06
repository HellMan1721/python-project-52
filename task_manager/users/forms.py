from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, label in self.Meta.labels.items():
            self.fields[field_name].label = label
        # убираем двоеточие
        for field in self.fields.values():
            field.label_suffix = ""
        
        self.fields['password1'].validators = []
        self.fields['password2'].validators = []
        self.fields['password1'].widget.attrs['minlength'] = 1
        self.fields['password2'].widget.attrs['minlength'] = 1