from django.shortcuts import render, redirect  # <--- Вставляем импорт сюда
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from dogs.models import Dog
from django.contrib import messages

@login_required
def user_profile(request):
    title = 'Профиль пользователя'
    dogs = Dog.objects.filter(owner=request.user)  # Получаем список собак текущего пользователя
    context = {
        'title': title,
        'dogs': dogs,  # Передаем список собак в контекст
    }
    return render(request, 'users/user_profile.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Передаем request и data
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)  # Исправлено: передаем username и password
            if user is not None:
                login(request, user)
                return redirect('dogs:index')  # Перенаправление после входа
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')  # Используем messages
                return render(request, 'users/login.html', {'form': form})
        else:
            return render(request, 'users/login.html', {'form': form, 'error': 'Неверные данные'})
    else:
        form = LoginForm(request)  # Передаем request
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Форма прошла валидацию!") # Отладочное сообщение
            try:
                user = form.save()  # Используем form.save()
                login(request, user)  # Вход в систему после регистрации
                return redirect('dogs:index')  # Перенаправляем на главную страницу
            except Exception as e:
                messages.error(request, f"Ошибка при регистрации: {e}") # Выводим сообщение об ошибке
                return render(request, 'users/register.html', {'form': form})
        else:
            print("Форма НЕ прошла валидацию!") # Отладочное сообщение
            print(form.errors) # Выводим ошибки
            return render(request, 'users/register.html', {'form': form, 'error': 'Неверные данные'})
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    django_logout(request)  # Выход из системы
    return redirect('dogs:index')  # Перенаправляем на главную страницу