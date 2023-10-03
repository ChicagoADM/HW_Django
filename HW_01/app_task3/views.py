import logging
import random
from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datetime_safe import datetime

from app_task2.models import Order, User


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a', format='%(levelname)s %(message)s')

def app_task3(request):
    logger.info(f'{request} request received')
    return HttpResponse("<h1>app_task3</h1>")

def basket(request, user_id):
    products = []
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user).all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'basket.html', {'user': user, 'orders': orders, 'products': products})


def sorted_basket(request, user_id, days_ago):
    products = []
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user, date_ordered__range=(before, now)).all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'basket.html', {'user': user, 'orders': orders, 'products': products})
