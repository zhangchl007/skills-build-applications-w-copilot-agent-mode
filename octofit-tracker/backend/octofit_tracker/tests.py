from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from octofit_tracker.models import ActivityLog, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class OctoFitModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123', email='test@example.com')
        self.team = Team.objects.create(name='Alpha Squad', description='Core training team')

    def test_create_related_models(self):
        profile = UserProfile.objects.create(user=self.user, team=self.team, age=29, fitness_goal='Build endurance')
        activity = ActivityLog.objects.create(
            user=self.user,
            activity_type='Running',
            duration_minutes=45,
            calories_burned=420,
            activity_date=date.today(),
        )
        leaderboard_entry = LeaderboardEntry.objects.create(user=self.user, total_points=980, rank=1)
        workout = WorkoutSuggestion.objects.create(
            user=self.user,
            title='Interval Run',
            description='5x 3-minute high-intensity intervals',
            target_goal='Build endurance',
            is_active=True,
        )

        self.assertEqual(str(profile.user), 'testuser')
        self.assertEqual(activity.activity_type, 'Running')
        self.assertEqual(leaderboard_entry.rank, 1)
        self.assertTrue(workout.is_active)


class OctoFitApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root_endpoint(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn('users', payload)
        self.assertIn('teams', payload)

    def test_root_points_to_api(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/api/')
