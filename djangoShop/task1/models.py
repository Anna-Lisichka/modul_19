from django.db import models


# Модели с отношением многие ко многим
# 1. модель представляющая покупателя
class Buyer(models.Model):
    name = models.CharField(max_length=100)  # username аккаунта
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # баланс
    age = models.PositiveIntegerField()  # возраст - только положительное значение


# 2. Модель представляющая игру
class Game(models.Model):
    title = models.CharField(max_length=200)  # название игры
    cost = models.DecimalField(max_digits=6, decimal_places=2)  # баланс
    size = models.DecimalField(max_digits=7, decimal_places=3)  # размер файлов игры
    description = models.TextField()  # описание игры
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer, related_name='games')

