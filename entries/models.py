from django.db import models

class Entry(models.Model):
  author = models.CharField(max_length=50)
  comment = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)
