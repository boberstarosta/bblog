from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=600)
	pub_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-pub_date']
