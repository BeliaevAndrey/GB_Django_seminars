from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('author_articles/<int:author_id>/', views.get_articles, name='get_articles'),
    path('get_article/<int:article_id>/', views.get_article, name='get_article'),
]
