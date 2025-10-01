from django.db import models
from django.conf import settings



class Article(models.Model):
	title = models.CharField(max_length=64, null=False, blank=False)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	synopsis = models.CharField(max_length=312, null=False, blank=False)
	content = models.TextField(null=False, blank=False)

	def __str__(self):
		return self.title
	
class UserFavoriteArticle(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites")
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="favorited_by")

	class Meta:
		unique_together = ("user", "article")

	def __str__(self):
		return self.article.title