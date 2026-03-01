from django.contrib.auth.models import User
from rest_framework import serializers

from octofit_tracker.models import ActivityLog, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class ObjectIdToStringModelSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)


class TeamSerializer(ObjectIdToStringModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at']


class UserProfileSerializer(ObjectIdToStringModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    team_id = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'user_id', 'team', 'team_id', 'age', 'fitness_goal']

    def get_team_id(self, obj):
        return str(obj.team_id) if obj.team_id else None


class ActivityLogSerializer(ObjectIdToStringModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = ActivityLog
        fields = [
            'id',
            'user',
            'user_id',
            'activity_type',
            'duration_minutes',
            'calories_burned',
            'activity_date',
        ]


class LeaderboardEntrySerializer(ObjectIdToStringModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'user_id', 'total_points', 'rank']


class WorkoutSuggestionSerializer(ObjectIdToStringModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'user', 'user_id', 'title', 'description', 'target_goal', 'is_active']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
