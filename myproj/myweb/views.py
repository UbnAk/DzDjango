# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.

# Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.

# Сохраняйте в логи данные о посещении страниц.
from django.shortcuts import render
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def home(request):
    html_text = '''
        <h1>Добро пожаловать!</h1>
        <p>Вы посетили мой первый Django - сайт</p>
    '''
    logger.info(f'Перешли на главную страницу.')
    return HttpResponse(html_text)


def info_about_me(request):
    html_text = '''
        <h2>Чуть-чуть обо мне.</h2>
        <p>Зовут меня Максим. Являюсь студентом GB.</p>
        <p>Мало времени на учёбу, но я стараюсь.</p>
        '''
    logger.info(f'Перешли на страницу с информацией обо мне.')
    return HttpResponse(html_text)

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return render(request, 'success.html', {'client_name': client.name})
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return render(request, 'success.html')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # Дополнительные операции с заказом
            order.save()
            return render(request, 'success.html')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})