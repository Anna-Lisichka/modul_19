from django.shortcuts import render
from .forms import UserRegister
from .models import *


# Создание функции, привязанной к шаблону Главной страницы.
def home_page(request):
    return render(request, 'platform.html')


# Создание функции, привязанной к шаблону Магазина.
def games(request):
    games_list = Game.objects.all()
    text = 'Купить'
    context = {
        'games_list': games_list,
        'text': text,
    }

    return render(request, 'games.html', context)


# Создание функции, привязанной к шаблону Корзина.
def cart(request):
    text1 = 'Выбрать способ оплаты'
    text2 = 'Выбрать способ получения '
    context = {
        'text1': text1,
        'text2': text2
    }
    return render(request, 'cart.html', context)


# Создание функции, привязанной к шаблону Главной страницы.
def menu(request):
    return render(request, 'menu.html')


# Создание функции для страницы регистрации
def sign_up_by_django(request):
    buyers = Buyer.objects.all() # получение покупателей из БД
    users = [buyer.name for buyer in buyers]
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        info['form'] = form
        if form.is_valid():
            info['username'] = form.cleaned_data["username"]
            info['password'] = form.cleaned_data["password"]
            info['repeat_password'] = form.cleaned_data["repeat_password"]
            info['age'] = form.cleaned_data["age"]

            if info['password'] == info['repeat_password'] and not users.count(info['username']):
                Buyer.objects.create(name=info['username'], age=info['age'], balance=0)
                info["generated"] = f"Приветствуем, {info['username']}!"
            elif users.count(info['username']):
                info["error"] = "Пользователь уже существует"
            elif info['password'] != info['repeat_password']:
                info["error"] = "Пароли не совпадают"
            else:
                info["error"] = "Вы должны быть старше 18"
        return render(request, template_name="registration_page.html", context=info)

    else:
        form = UserRegister()
    return render(request, 'registration_page.html', context={'form': form})
