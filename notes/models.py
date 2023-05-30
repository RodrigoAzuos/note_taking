from django.db import models

# Create your models here.

class Note(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=64)
	description = models.TextField(max_length=256)
	done = models.BooleanField(default=False)

