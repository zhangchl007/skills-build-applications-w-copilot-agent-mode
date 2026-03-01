from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index({'email': 1}, unique=True)

        # Sample data
        users = [
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'team': 'Marvel'},
        ]
        teams = [
            {'name': 'Marvel', 'members': ['Iron Man', 'Captain America', 'Black Widow']},
            {'name': 'DC', 'members': ['Superman', 'Batman', 'Wonder Woman']},
        ]
        activities = [
            {'user': 'Superman', 'activity': 'Flight', 'duration': 120},
            {'user': 'Iron Man', 'activity': 'Suit Training', 'duration': 90},
        ]
        leaderboard = [
            {'team': 'Marvel', 'points': 250},
            {'team': 'DC', 'points': 200},
        ]
        workouts = [
            {'user': 'Batman', 'workout': 'Martial Arts', 'intensity': 'High'},
            {'user': 'Black Widow', 'workout': 'Spy Training', 'intensity': 'Medium'},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Team, UserProfile, ActivityLog, LeaderboardEntry, WorkoutSuggestion
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        WorkoutSuggestion.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        ActivityLog.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Super Heroes')
        dc = Team.objects.create(name='DC', description='DC Super Heroes')

        # Super heroes
        heroes = [
            # Marvel
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'age': 45, 'goal': 'Build tech muscle', 'team': marvel},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'age': 18, 'goal': 'Improve agility', 'team': marvel},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'age': 100, 'goal': 'Endurance', 'team': marvel},
            # DC
            {'username': 'batman', 'email': 'batman@dc.com', 'age': 35, 'goal': 'Peak strength', 'team': dc},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'age': 3000, 'goal': 'Immortal fitness', 'team': dc},
            {'username': 'flash', 'email': 'flash@dc.com', 'age': 25, 'goal': 'Speed', 'team': dc},
        ]

        for h in heroes:
            user = User.objects.create_user(username=h['username'], email=h['email'], password='SuperSecret123!')
            UserProfile.objects.create(user=user, team=h['team'], age=h['age'], fitness_goal=h['goal'])
            ActivityLog.objects.create(user=user, activity_type='Training', duration_minutes=60, calories_burned=500, activity_date=date.today())
            LeaderboardEntry.objects.create(user=user, total_points=1000, rank=1)
            WorkoutSuggestion.objects.create(user=user, title='Hero Workout', description=f"Special plan for {h['username']}", target_goal=h['goal'], is_active=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with super hero test data.'))
