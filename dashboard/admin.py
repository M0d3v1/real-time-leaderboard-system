from django.contrib import admin
from .models import UserProfile, LeaderboardEntry, Transaction, Analytics

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_premium', 'points')

@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'date_achieved')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'transaction_type', 'date')

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
