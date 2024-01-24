# Generated by Django 4.2.7 on 2023-11-27 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('bio', models.TextField(blank=True)),
                ('home_church', models.CharField(max_length=100)),
                ('profile_img', models.ImageField(default='blank_profile_picture.png', upload_to='profile_images')),
                ('denomination', models.CharField(choices=[('Catholic', 'Catholic'), ('Protestant', 'Protestant'), ('Orthodox', 'Orthodox'), ('Anglican', 'Anglican'), ('Baptist', 'Baptist'), ('Methodist', 'Methodist'), ('Lutheran', 'Lutheran'), ('Presbyterian', 'Presbyterian'), ('Pentecostal', 'Pentecostal'), ('Episcopalian', 'Episcopalian'), ('Nondenominational', 'Nondenominational'), ('Assemblies of God', 'Assemblies of God'), ('Seventh-day Adventist', 'Seventh-day Adventist'), ('Evangelical', 'Evangelical'), ('Reformed', 'Reformed'), ('Congregational', 'Congregational'), ('Anabaptist', 'Anabaptist'), ('United Church of Christ', 'United Church of Christ'), ('Unitarian Universalist', 'Unitarian Universalist'), ('Denomination Neutral', 'Denomination Neutral')], default='Denomination Neutral', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
