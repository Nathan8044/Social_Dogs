# Generated by Django 4.2.7 on 2023-12-26 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_video_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]
