from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
    score = models.IntegerField(blank=True)
    total = models.IntegerField(blank=True)
    user = models.ManyToManyField(User, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    percent = models.IntegerField(blank=True)

    class Meta:
        ordering = ['-added']

