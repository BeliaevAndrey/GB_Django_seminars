from django.shortcuts import render, get_object_or_404
from datetime import datetime as dt, timedelta

from homewrk_02.models import Customer, Product, Order


# Задание No7
#
# * Доработаем задачу 8 из прошлого семинара про клиентов, товары и заказы.
# * Создайте шаблон для вывода всех заказов клиента и списком товаров
#   внутри каждого заказа.
# * Подготовьте необходимый маршрут и представление.
#
# Домашнее задание
# * Продолжаем работать с товарами и заказами.
# * Создайте шаблон, который выводит список заказанных клиентом товаров
#   из всех его заказов с сортировкой по времени:
#       * за последние 7 дней (неделю)
#       * за последние 30 дней (месяц)
#       * за последние 365 дней (год)
# * *Товары в списке не должны повторятся.


def order_list(request, customer_id):
    """
    List of orders for customer with lists of products
    :param request:
    :param customer_id: int     -- customer id
    :return:
    """
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    context = {'customer': customer, }
    if orders:
        context['orders'] = []
        for order in orders:
            context['orders'].append(
                {
                    'order': order,
                    'products': [item for item in order.product.all()],
                }
            )
    return render(request, 'homewrk_02/hw02_orders.html', context=context)


def ordered_products_list(request, customer_id, period):
    """
    Show products list form orders for defined period
    :param request:
    :param customer_id: int
    :param period: str      -- 'week', 'month' or 'year'
    :return:
    """
    customer = get_object_or_404(Customer, pk=customer_id)

    limit = 7 if period == 'week' else 30 if period == 'month' else 365 if period == 'year' else 0

    date_low_lim = (dt.now() - timedelta(limit + 1)).strftime("%Y-%m-%d")
    print(date_low_lim)
    if not limit:
        orders = Order.objects.filter(customer=customer).order_by('-order_date')
    else:
        orders = Order.objects.filter(customer=customer).filter(order_date__gt=date_low_lim).order_by('pk')
    context = {'customer': customer, }
    if orders:
        context['products'] = []
        for order in orders:
            context['products'].extend(
                [
                    {
                        'pk': item.pk,
                        'name': item.name,
                        'price': item.price,
                        'date': order.order_date,
                    }
                    for item in order.product.all()
                ]
            )
    return render(request, 'homewrk_02/hw02_ordered_products.html', context=context)


def ordered_products_unique(request, customer_id, period):
    """
    Show non-repeated products list form orders for defined period
    :param request:
    :param customer_id: int
    :param period: str      -- 'week', 'month' or 'year'
    :return:
    """
    customer = get_object_or_404(Customer, pk=customer_id)

    limit = 7 if period == 'week' else 30 if period == 'month' else 365 if period == 'year' else 0

    date_low_lim = (dt.now() - timedelta(limit + 1)).strftime("%Y-%m-%d")
    print(date_low_lim)
    if not limit:
        orders = Order.objects.filter(customer=customer).order_by('-order_date')
    else:
        orders = Order.objects.filter(customer=customer).filter(order_date__gt=date_low_lim).order_by('-order_date')
    context = {'customer': customer, }
    if orders:
        products_total = set()
        for order in orders:
            products_total.update([*order.product.all()])
        context['products'] = [
            {
                'pk': item.pk,
                'name': item.name,
                'price': item.price,
            }
            for item in sorted(products_total, key=lambda x: x.price)
        ]
    return render(request, 'homewrk_02/hw02_ordered_products_unique.html', context=context)


# Customers ids for test:
# 18 -- 1 order
# 19 -- 1 order
# 20 -- many orders, long time period (year)
# 21 -- 3 orders, short time period (week), similar products in different orders
# 23 -- 2 orders, short time period (week)
