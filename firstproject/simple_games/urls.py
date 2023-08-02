from django.urls import path
from . import views


urlpatterns = [
    path('simple_games/', views.games_index, name='index'),
    path('simple_games/coinplay/', views.coin, name='coinplay'),
    path('simple_games/diceplay/', views.dice, name='diceplay'),
    path('simple_games/randomizer/', views.random_number, name='random_number'),
    path('simple_games/coinplay_records/<int:amount>/', views.coin_records, name='coinplay_records'),
    path('simple_games/diceplay_records/<int:amount>', views.dice_records, name='diceplay_records'),
    path('simple_games/randomizer_records/<int:amount>', views.random_number_records, name='random_number_records'),
]
