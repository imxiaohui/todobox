from django.db import models
from django.contrib.auth.models import User

class TaskBox(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=100)

	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-pub_date']

	def get_tasks(self):
		return Task.objects.filter(box__pk = self.pk)

class Task(models.Model):
	box = models.ForeignKey(TaskBox)
	title = models.CharField(max_length=200)

	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-pub_date']