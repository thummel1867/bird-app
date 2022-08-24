from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('articles/<int:article_id>/', views.article_detail, name='article'),
    path('author/<int:author_id>', views.author_details, name="author_id"),
    path('topics/<int:topic_id>', views.get_by_topic, name="topic_id")
]   
