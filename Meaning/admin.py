from django.contrib import admin
from .models import Word, Meaning, Note

# Register your models here.
admin.site.register(Word)
admin.site.register(Meaning)
admin.site.register(Note)