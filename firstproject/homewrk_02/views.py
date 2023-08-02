from django.shortcuts import render, get_object_or_404

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
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = list(Order.objects.filter(customer=customer))
    context = {'customer': customer,}
    if orders:
        context['orders'] = []
        for order in orders:
            context['orders'].append(
                {
                    'order': order,
                    'products': [item for item in order.product.all()]
                 }
            )
    return render(request, 'homewrk_02/hw02_orders.html', context=context)

