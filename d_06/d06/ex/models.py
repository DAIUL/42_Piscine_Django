from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserInfos(AbstractUser):

	def score_calculation(self):
		tips = self.tips.all()
		score = 0
		for tip in tips:
			score += tip.upvoted_count() * 5
			score -= tip.downvoted_count() * 2
		return score

	def __str__(self):
		return f"{self.username} ({self.score_calculation()} pts)"
	
class Tip(models.Model):

	content = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tips")
	created_at = models.DateTimeField(auto_now_add=True)
	upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="upvoted_tips", blank=True)
	downvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="downvoted_tips", blank=True)

	class Meta:
		permissions = [
			("downvote_tip", "Can downvote a tip")
		]

	def upvoted_count(self):
		return self.upvotes.count()

	def downvoted_count(self):
		return self.downvotes.count()

	def __str__(self):
		return f"Tip by {self.author.username} at {self.created_at}"