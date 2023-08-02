from django.urls import path
from . import views


urlpatterns = [
    path('orders/<int:customer_id>/', views.order_list, name='orders_list'),
]
