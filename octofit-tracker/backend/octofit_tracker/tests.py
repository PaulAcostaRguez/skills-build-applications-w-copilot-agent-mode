from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
	def setUp(self):
		self.team = Team.objects.create(name="Avengers", universe="Marvel")
		self.user = User.objects.create(name="Tony Stark", email="tony@stark.com", team=self.team)
		self.workout = Workout.objects.create(name="Pushups", description="Pushups routine", difficulty="Easy")
		self.activity = Activity.objects.create(user=self.user, type="Running", duration=30, date="2026-05-13")
		self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, position=1)

	def test_team_str(self):
		self.assertEqual(str(self.team), "Avengers")

	def test_user_str(self):
		self.assertEqual(str(self.user), "Tony Stark")

	def test_workout_fields(self):
		self.assertEqual(self.workout.difficulty, "Easy")

	def test_activity_duration(self):
		self.assertEqual(self.activity.duration, 30)

	def test_leaderboard_score(self):
		self.assertEqual(self.leaderboard.score, 100)
