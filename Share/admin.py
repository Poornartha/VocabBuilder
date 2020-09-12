from django.contrib import admin
from .models import Community, Post, Comment, Image

# Register your models here.
admin.site.register(Community)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Image)
