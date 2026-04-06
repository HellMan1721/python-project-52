from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", max_length=150)
    last_name = forms.CharField(label="Фамилия", max_length=150)
    username = forms.CharField(label="Имя пользователя", max_length=150)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)    


    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, label in self.Meta.labels.items():
                self.fields[field_name].label = label
            # убираем двоеточие
            for field in self.fields.values():
                field.label_suffix = ""