# Generated by Django 3.1 on 2020-09-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='total',
            field=models.IntegerField(blank=True, default=10),
            preserve_default=False,
        ),
    ]
