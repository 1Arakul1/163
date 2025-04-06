from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User  # Важно: импортируем вашу кастомную модель!

class LoginForm(AuthenticationForm):
    """
    Форма для входа пользователя.
    Использует AuthenticationForm из django.contrib.auth.forms для обработки аутентификации.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].label = 'Пароль'


class RegisterForm(UserCreationForm):
    """
    Форма для регистрации нового пользователя.
    Наследуется от UserCreationForm и добавляет поля email, first_name и last_name.
    """
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя', max_length=30, required=False)  # Добавлено поле
    last_name = forms.CharField(label='Фамилия', max_length=150, required=False)  # Добавлено поле

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")  # Указываем поля, которые будут отображаться в форме

    def clean_username(self):
        """
        Проверяет, что имя пользователя еще не занято.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Это имя пользователя уже занято.")
        return username

    def save(self, commit=True):
        """
        Сохраняет пользователя и устанавливает имя и фамилию.
        """
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        if commit:
            user.save()
        return user