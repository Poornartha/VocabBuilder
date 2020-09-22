from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Community(models.Model):
    user = models.ManyToManyField(User, blank=True)
    name = models.TextField()
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Community, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.TextField(max_length=100)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    visiblity = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='PostImages')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Mata:
        ordering = ['timestamp']







