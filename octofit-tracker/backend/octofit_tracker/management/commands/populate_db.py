from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection
from pymongo import MongoClient

# Sample data for population
USERS = [
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
]

TEAMS = [
    {"name": "Marvel", "members": ["Iron Man", "Captain America", "Spider-Man"]},
    {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
]

ACTIVITIES = [
    {"user": "Iron Man", "activity": "Running", "duration": 30},
    {"user": "Batman", "activity": "Cycling", "duration": 45},
    {"user": "Wonder Woman", "activity": "Swimming", "duration": 60},
]

LEADERBOARD = [
    {"team": "Marvel", "points": 250},
    {"team": "DC", "points": 200},
]

WORKOUTS = [
    {"name": "Full Body Blast", "suggested_for": "Marvel"},
    {"name": "Hero HIIT", "suggested_for": "DC"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Ensure unique index on email
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
