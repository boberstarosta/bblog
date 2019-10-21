from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=600)
	pub_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', args=[self.pk])

	class Meta:
		ordering = ['-pub_date']
