from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from octofit_tracker.models import ActivityLog, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion
from octofit_tracker.serializers import (
    ActivityLogSerializer,
    LeaderboardEntrySerializer,
    TeamSerializer,
    UserProfileSerializer,
    WorkoutSuggestionSerializer,
)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.select_related('user', 'team').all().order_by('user__username')
    serializer_class = UserProfileSerializer


class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.select_related('user').all().order_by('-activity_date')
    serializer_class = ActivityLogSerializer


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.select_related('user').all().order_by('rank')
    serializer_class = LeaderboardEntrySerializer


class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.select_related('user').all().order_by('title')
    serializer_class = WorkoutSuggestionSerializer


router = DefaultRouter()
router.register('teams', TeamViewSet)
router.register('profiles', UserProfileViewSet)
router.register('activities', ActivityLogViewSet)
router.register('leaderboard', LeaderboardEntryViewSet)
router.register('workouts', WorkoutSuggestionViewSet)


@api_view(['GET'])
def api_root(request):
    return Response(
        {
            'teams': request.build_absolute_uri('teams/'),
            'profiles': request.build_absolute_uri('profiles/'),
            'activities': request.build_absolute_uri('activities/'),
            'leaderboard': request.build_absolute_uri('leaderboard/'),
            'workouts': request.build_absolute_uri('workouts/'),
        },
        status=status.HTTP_200_OK,
    )
