# Generated by Django 3.1 on 2020-08-27 06:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Share', '0002_auto_20200827_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
