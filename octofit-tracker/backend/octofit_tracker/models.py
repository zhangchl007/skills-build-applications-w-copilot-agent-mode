from django.contrib.auth.models import User
from djongo import models


class Team(models.Model):
    id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    age = models.PositiveIntegerField(default=18)
    fitness_goal = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


class ActivityLog(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=80)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField(default=0)
    activity_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"


class LeaderboardEntry(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard_entry')
    total_points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} (Rank {self.rank})"


class WorkoutSuggestion(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_suggestions')
    title = models.CharField(max_length=120)
    description = models.TextField()
    target_goal = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
