from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = "Entries"
