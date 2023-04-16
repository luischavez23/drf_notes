from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)