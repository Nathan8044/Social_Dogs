from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    id_user = models.IntegerField()

    bio = models.TextField(blank=True)

    home_church = models.CharField(max_length=100)

    profile_img = models.ImageField(upload_to='profile_images', default='blank_profile_picture.png')

    user_type = models.CharField(max_length=100, default='user')

    location = models.TextField(blank=True)
    senior_pastor = models.TextField(blank=True)

    introductory_video_file = models.FileField(upload_to='introductory-videos', blank=True)

    church_banner = models.ImageField(upload_to='church_banners', default='blank_banner.png')

    founded_date = models.TextField(blank=True)


    CATHOLIC = 'Catholic'
    PROTESTANT = 'Protestant'
    ORTHODOX = 'Orthodox'
    ANGLICAN = 'Anglican'
    BAPTIST = 'Baptist'
    METHODIST = 'Methodist'
    LUTHERAN = 'Lutheran'
    PRESBYTERIAN = 'Presbyterian'
    PENTECOSTAL = 'Pentecostal'
    EPISCOPALIAN = 'Episcopalian'
    NONDENOMINATIONAL = 'Nondenominational'
    ASSEMBLIES_OF_GOD = 'Assemblies of God'
    SEVENTH_DAY_ADVENTIST = 'Seventh-day Adventist'
    EVANGELICAL = 'Evangelical'
    REFORMED = 'Reformed'
    CONGREGATIONAL = 'Congregational'
    ANABAPTIST = 'Anabaptist'
    UNITED_CHURCH_OF_CHRIST = 'United Church of Christ'
    UNITARIAN_UNIVERSALIST = 'Unitarian Universalist'
    DENOMINATION_NEUTRAL = 'Denomination Neutral'

    # Continue adding denominations as needed

    CHOICES = [
        (CATHOLIC, 'Catholic'),
        (PROTESTANT, 'Protestant'),
        (ORTHODOX, 'Orthodox'),
        (ANGLICAN, 'Anglican'),
        (BAPTIST, 'Baptist'),
        (METHODIST, 'Methodist'),
        (LUTHERAN, 'Lutheran'),
        (PRESBYTERIAN, 'Presbyterian'),
        (PENTECOSTAL, 'Pentecostal'),
        (EPISCOPALIAN, 'Episcopalian'),
        (NONDENOMINATIONAL, 'Nondenominational'),
        (ASSEMBLIES_OF_GOD, 'Assemblies of God'),
        (SEVENTH_DAY_ADVENTIST, 'Seventh-day Adventist'),
        (EVANGELICAL, 'Evangelical'),
        (REFORMED, 'Reformed'),
        (CONGREGATIONAL, 'Congregational'),
        (ANABAPTIST, 'Anabaptist'),
        (UNITED_CHURCH_OF_CHRIST, 'United Church of Christ'),
        (UNITARIAN_UNIVERSALIST, 'Unitarian Universalist'),
        (DENOMINATION_NEUTRAL, 'Denomination Neutral')
    ]

    # Define a CharField with choices
    denomination = models.CharField(
        max_length=50,
        choices=CHOICES,
        default=DENOMINATION_NEUTRAL,  # You can set a default value if needed
    )

from django.db import models

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming User is another model representing a user
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails', default='blank_thumbnail.png')
    date_published = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='video-content')  # Assuming you want to upload and store video files

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assu1ming User is another model representing a user
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    text_content = models.TextField(blank=True)
    image = models.ImageField(upload_to='post-images')  # Assuming you want to upload and store images


