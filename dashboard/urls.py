from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('user/<int:user_id>/', views.user_profile_view, name='user_profile'),
]
