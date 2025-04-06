from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from dogs.models import Dog
from django.contrib import messages

@login_required
def user_profile(request):
    """
    Представление для просмотра профиля пользователя,
    включая информацию об аккаунте и список любимых собак.
    """
    title = 'Профиль пользователя'
    user = request.user  # Получаем текущего пользователя
    dogs = Dog.objects.filter(owner=request.user)

    context = {
        'title': title,
        'user': user,  # Передаем информацию о пользователе в контекст
        'dogs': dogs,
    }
    return render(request, 'users/user_profile.html', context)

@login_required
def account_info(request):
    """
    Представление для отображения информации об аккаунте.
    """
    title = "Информация об аккаунте"
    user = request.user  # Получаем текущего пользователя
    context = {
        'title': title,
        'user': user,
    }
    return render(request, 'users/account_info.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dogs:index')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
                return render(request, 'users/login.html', {'form': form})
        else:
            return render(request, 'users/login.html', {'form': form, 'error': 'Неверные данные'})
    else:
        form = LoginForm(request)
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Форма прошла валидацию!")
            try:
                user = form.save()
                login(request, user)
                return redirect('dogs:index')
            except Exception as e:
                messages.error(request, f"Ошибка при регистрации: {e}")
                return render(request, 'users/register.html', {'form': form})
        else:
            print("Форма НЕ прошла валидацию!")
            print(form.errors)
            return render(request, 'users/register.html', {'form': form, 'error': 'Неверные данные'})
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    django_logout(request)
    return redirect('dogs:index')