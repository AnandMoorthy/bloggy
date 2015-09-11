from django.db import models
from django.utils import timezone

class Blog(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	posted = models.DateTimeField()


