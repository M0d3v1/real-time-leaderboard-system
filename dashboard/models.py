from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Constants for choices
class TransactionTypes:
    PURCHASE = 'purchase'
    REWARD = 'reward'
    REFUND = 'refund'
    TYPES = [
        (PURCHASE, 'Purchase'),
        (REWARD, 'Reward'),
        (REFUND, 'Refund')
    ]

class UserProfileManager(models.Manager):
    def active_users(self):
        return self.filter(user__is_active=True)

class LeaderboardManager(models.Manager):
    def top_users(self, limit=10):
        return self.order_by('-score')[:limit]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    
    # Add manager for additional query methods
    objects = UserProfileManager()

    def __str__(self):
        return self.user.username

    def add_points(self, points):
        """Business logic to add points to user."""
        self.points += points
        self.save()

    def reset_points(self):
        """Reset points to zero."""
        self.points = 0
        self.save()

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_achieved = models.DateTimeField(default=timezone.now)

    # Custom manager for leaderboard-specific queries
    objects = LeaderboardManager()

    def __str__(self):
        return f"{self.user} - {self.score} points"

    class Meta:
        ordering = ['-score']

class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=50, choices=TransactionTypes.TYPES
    )
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.get_transaction_type_display()}: ${self.amount}"

class Analytics(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)  # 'login', 'play', etc.
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"
