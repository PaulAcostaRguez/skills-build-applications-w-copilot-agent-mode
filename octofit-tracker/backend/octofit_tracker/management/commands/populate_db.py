from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Eliminar datos existentes
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Crear usuarios (superhéroes)
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Crear actividades
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now())
        Activity.objects.create(user=users[2], type='Swimming', duration=25, date=timezone.now())
        Activity.objects.create(user=users[3], type='Yoga', duration=60, date=timezone.now())

        # Crear workouts
        Workout.objects.create(name='Full Body', description='Entrenamiento completo', difficulty='Medium')
        Workout.objects.create(name='Cardio Blast', description='Cardio intenso', difficulty='Hard')

        # Crear leaderboard
        Leaderboard.objects.create(user=users[0], score=100, position=1)
        Leaderboard.objects.create(user=users[1], score=90, position=2)
        Leaderboard.objects.create(user=users[2], score=80, position=3)
        Leaderboard.objects.create(user=users[3], score=70, position=4)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
