# Generated by Django 4.2.7 on 2024-01-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='senior_pastor',
            field=models.TextField(blank=True),
        ),
    ]
