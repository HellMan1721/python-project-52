from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", max_length=150)
    last_name = forms.CharField(label="Фамилия", max_length=150)
    username = forms.CharField(label="Имя пользователя", max_length=150)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ""

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        # только проверка совпадения, без сложных правил
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")

        return password2

    def _post_clean(self):
        """Отключаем стандартную валидацию пароля Django"""
        pass