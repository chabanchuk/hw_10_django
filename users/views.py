# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required

# ... ваш код для реєстрації та входу ...

@login_required
def user_logout(request):
    logout(request)
    return redirect('toscrape_app:main')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Перевірка, чи паролі співпадають
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                # Створення нового користувача з хешованим паролем
                new_user = User.objects.create_user(
                    username=form.cleaned_data['Username'],
                    password=form.cleaned_data['password1']
                )
                new_user.save()
                return redirect('toscrape_app:main')
            else:
                form.add_error('password2', 'Паролі не співпадають')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('toscrape_app:main')
            else:
                form.add_error(None, 'Невірний логін або пароль')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})