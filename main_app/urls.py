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
    path('user/', views.user_detail, name="user_page"),
    path('user/<int:user_id>/', views.user_page, name='account_page'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path('bird/seen/<int:bird_id>/assoc_user/<int:user_id>/', views.seen_bird, name = "seen_bird"),
    path('bird/searching/<int:bird_id>/assoc_user/<int:user_id>/', views.searching_bird, name = "searching_bird"),
    path('bird/seen/<int:bird_id>/unassoc_user/<int:user_id>/', views.unassoc_seen_bird, name = "remove_seen_bird"),
    path('bird/searching/<int:bird_id>/unassoc_user/<int:user_id>/', views.unassoc_searching_bird, name = "remove_searching_bird"),
    path('bird/searching/<int:bird_id>/move/<int:user_id>/', views.move_searching_bird, name = "move_searching_bird")
]   
