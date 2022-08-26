from django.urls import path, include
from . import views


app_name = 'main_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('bird/<int:bird_id>/', views.bird_detail, name='bird'),
    path('bird/create/', views.BirdCreate.as_view(), name='bird_create'),
    path('bird/<int:pk>/delete/', views.BirdDelete.as_view(), name='bird_delete'),
    path('bird/<int:pk>/update/', views.BirdUpdate.as_view(), name='bird_update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('user/', views.user_detail, name="user_page")
]   
