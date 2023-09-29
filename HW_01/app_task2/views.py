import logging
import random
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render

from app_task2.models import User, Product, Order

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a', format='%(levelname)s %(message)s')


def app_task2(request):
    logger.info(f'{request} request received')
    return HttpResponse('<h1>app_task2</h1>')



def user_read(request):
    logger.info(f'{request} request received')
    user = User.objects.all()
    return HttpResponse(user)


def user_create(request):
    logger.info(f'{request} request received')
    user_name = request.GET.get('name')
    user = User(name=user_name,
                email=f'{user_name}@mail.com',
                phone=f'2-12-85-06',
                address=f'Wall street',
                reg_date=timezone.now())
    user.save()
    return HttpResponse(user)


def user_update(request):
    logger.info(f'{request} request received')
    user_id = request.GET.get('user_id')
    user = User.objects.filter(id=user_id).first()
    user.name = 'new_user_name'
    user.save()
    return HttpResponse(user)


def user_delete(request):
    logger.info(f'{request} request received')
    user_id = request.GET.get('user_id')
    user = Comment.objects.filter(id=user_id).first()
    user.delete()
    return HttpResponse(user)


def product_read(request):
    logger.info(f'{request} request received')
    product = Product.objects.all()
    return HttpResponse(product)


def product_create(request):
    logger.info(f'{request} request received')
    product_name = request.GET.get('name')
    product = Product(name=product_name,
                      description=f'{product_name} description',
                      price=random.randint(1, 100),
                      prod_quant=random.randint(1, 10),
                      reg_date=timezone.now())
    product.save()
    return HttpResponse(product)


def product_update(request):
    logger.info(f'{request} request received')
    product_id = request.GET.get('product_id')
    product = Product.objects.filter(id=product_id).first()
    product.name = 'new_product'
    product.save()
    return HttpResponse(product)


def product_delete(request):
    logger.info(f'{request} request received')
    product_id = request.GET.get('product_id')
    product = Product.objects.filter(id=product_id).first()
    product.delete()
    return HttpResponse(product)


def order_read(request):
    logger.info(f'{request} request received')
    order = Order.objects.all()
    return HttpResponse(order)


def order_create(request):
    logger.info(f'{request} request received')
    user_id = request.GET.get('user_id')
    product_id = request.GET.get('product_id')
    user = Order.objects.filter(id=user_id).first()
    product = Order.objects.filter(id=product_id).first()
    order = Order(customer=user,
                  products=product,
                  total_price=product.price,
                  date_ordered=timezone.now())
    order.save()
    return HttpResponse(order)


def order_update(request):
    logger.info(f'{request} request received')
    order_id = request.GET.get('order_id')
    user_id = request.GET.get('user_id')
    order = Order.objects.filter(id=order_id).first()
    order.customer = user_id
    order.save()
    return HttpResponse(order)


def order_delete(request):
    logger.info(f'{request} request received')
    order_id = request.GET.get('order_id')
    order = Order.objects.filter(id=order_id).first()
    order.delete()
    return HttpResponse(order)
