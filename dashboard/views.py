from django.shortcuts import render
from .models import UserProfile, LeaderboardEntry

def leaderboard_view(request):
    # Fat models, skinny views approach
    top_users = LeaderboardEntry.objects.top_users(limit=10)
    return render(request, 'leaderboard.html', {'top_users': top_users})

def user_profile_view(request, user_id):
    user_profile = UserProfile.objects.get(pk=user_id)
    return render(request, 'profile.html', {'user_profile': user_profile})
