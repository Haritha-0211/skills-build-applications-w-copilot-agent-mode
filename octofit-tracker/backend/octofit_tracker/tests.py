from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name="Test User", email="test@example.com", team="Test Team")

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Test User")

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Test Team", members=["Test User"])

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.activity = Activity.objects.create(user="Test User", activity="Running", duration=30)

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity, "Running")

class LeaderboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.leaderboard = Leaderboard.objects.create(team="Test Team", points=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(name="Push Ups", suggested_for="All")

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Push Ups")
