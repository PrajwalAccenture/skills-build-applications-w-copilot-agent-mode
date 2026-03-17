from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='marvel')
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='marvel')
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc')
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc')

        # Activities
        Activity.objects.create(user=tony, activity_type='run', duration=30, date=date(2023,1,1))
        Activity.objects.create(user=steve, activity_type='cycle', duration=45, date=date(2023,1,2))
        Activity.objects.create(user=bruce, activity_type='swim', duration=25, date=date(2023,1,3))
        Activity.objects.create(user=clark, activity_type='run', duration=60, date=date(2023,1,4))

        # Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', suggested_for='marvel')
        Workout.objects.create(name='Flight Training', description='Flight workout for heroes', suggested_for='dc')

        # Leaderboard
        Leaderboard.objects.create(user=tony, score=100, rank=1)
        Leaderboard.objects.create(user=steve, score=90, rank=2)
        Leaderboard.objects.create(user=bruce, score=95, rank=1)
        Leaderboard.objects.create(user=clark, score=85, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
