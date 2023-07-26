from django.urls import path
from . import views


urlpatterns = {
    path('', views.index, name='index'),
    path('coinplay/', views.coin, name='coinplay'),
    path('diceplay/', views.dice, name='diceplay'),
    path('randomizer/', views.random_number, name='random_number'),
}
