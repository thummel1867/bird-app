from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('articles/', views.articles_index, name="articles"),
    path('articles/<int:article_id>/', views.articles_index, name="article_id")
]

