from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views





urlpatterns = [
    path("login/", views.user_login, name='user_login'),
    path("signup/", views.signup, name='signup'),
    path("", views.user_profile, name='user_profile'),
    path("user_profile/", views.user_profile, name='user_profile'),
    path('logout/', views.logout_user, name='logout_user'),
    path('create-content/', views.create_content, name="create_content"),
    path('watch-video/<int:video_id>/', views.watch_video, name='watch_video'),
    path('other_user_profile/<str:username>/', views.other_user_profile, name='other_user_profile'),



]


