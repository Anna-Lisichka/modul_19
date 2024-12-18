"""
URL configuration for djangoShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task1.views import *   # импорт функций для регистрации

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/games', games),  # запуск страницы с играми
    path('platform/cart', cart),  # запуск страницы корзины
    path('platform/', home_page),  # запуск главной страницы
    path('', sign_up_by_django),  # маршрут для запуска страницы-регистрации

]
