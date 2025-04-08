from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(email='zerocool@mhigh.edu', name='Elliot Alderson', age=28),
            User(email='crashoverride@mhigh.edu', name='Dade Murphy', age=25),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token', age=22),
        ]

        # Save users individually to ensure they are persisted
        for user in users:
            user.save()

        # Create teams
        teams = [
            Team(name='Blue Team', members=[users[0].id, users[1].id]),
            Team(name='Gold Team', members=[users[2].id, users[3].id, users[4].id]),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date='2025-04-08'),
            Activity(user=users[1], type='Crossfit', duration=120, date='2025-04-07'),
            Activity(user=users[2], type='Running', duration=90, date='2025-04-06'),
            Activity(user=users[3], type='Strength', duration=30, date='2025-04-05'),
            Activity(user=users[4], type='Swimming', duration=75, date='2025-04-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], points=100),
            Leaderboard(user=users[1], points=90),
            Leaderboard(user=users[2], points=95),
            Leaderboard(user=users[3], points=85),
            Leaderboard(user=users[4], points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(name='Running Training', description='Training for a marathon', duration=90),
            Workout(name='Strength Training', description='Training for strength', duration=30),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))