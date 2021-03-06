# Generated by Django 3.1 on 2020-08-27 05:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('uid', models.UUIDField()),
                ('admin', models.ManyToManyField(blank=True, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
