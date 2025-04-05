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
    Наследуется от UserCreationForm и добавляет поле email.
    """
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ("username", "email")  # Указываем поля, которые будут отображаться в форме

    def clean_username(self):
        """
        Проверяет, что имя пользователя еще не занято.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Это имя пользователя уже занято.")
        return username