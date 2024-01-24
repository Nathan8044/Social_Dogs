from django.contrib import admin
from . import models

# Register your models here.


class SocialProfile(admin.ModelAdmin):

    list_display = ['user', 'bio', 'home_church', 'profile_img', 'denomination']



class VideoContent(admin.ModelAdmin):

    list_display = ['user', 'profile', 'title', 'description', 'video_file', 'thumbnail', 'date_published']
admin.site.register(models.Profile, SocialProfile)
admin.site.register(models.Video, VideoContent)
admin.site.register(models.Post)
