from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Word(models.Model):
    user = models.ManyToManyField(User, blank=True)
    word = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.word
    

class Meaning(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    meaning = models.TextField()
    pos = models.TextField(blank=True)

    def __str__(self):
        return self.meaning

class Note(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()


