from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from core.models import Profile, Video


# Create your views here.


@login_required(login_url='login/')
def index(request):

    user_info = Profile.objects.get(user=request.user)


    return render(request, 'index.html', {'username': user_info.user.username})



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')



        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('/user_profile')
        
        else: 
            messages.info(request, 'Credentials invalid')

            return redirect('/login')



    return render(request, 'login.html',)

def signup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        type = request.POST.get('church')

        if type == 'user':
            user_type = 'user'
        else: 

            user_type = 'church'




        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
        else: 


            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user_login = auth.authenticate(username=username, password=password)
            auth.login(request, user_login)

            user_model = User.objects.get(username=username)
            
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, user_type=user_type)

            new_profile.save()

            return redirect('user_profile')

     

    else: 

        return render(request, 'signup.html')






@login_required(login_url='login/')
def user_profile(request):
    user_info = Profile.objects.get(user=request.user)
    user_videos = Video.objects.filter(user=request.user).order_by('date_published')

    # video_info_list = [{'thumbnail': video.thumbnail.url, 'video_file': video.video_file.url} for video in user_video_info]

    if request.method == 'POST':
            if user_info.user_type == 'user':

                profile_image = request.FILES.get('upload-new-profile-image')
                username = request.POST.get('username')
                bio = request.POST.get('bio')
                home_church = request.POST.get('home_church')
                denomination = request.POST.get('denomination')

                if profile_image: 
                    user_info.profile_img = profile_image
                if username:
                    user_info.user.username = username 
                    user_info.user.save()
                if bio: 
                    user_info.bio = bio
                if home_church: 
                    user_info.home_church = home_church
                if denomination:
                    user_info.denomination = denomination
                user_info.save()
                return render(request, 'user_profile.html', {        
                    'username': user_info.user,
                    'profile_photo': user_info.profile_img,
                    'base_church': user_info.home_church,
                    'denomination': user_info.denomination,
                    'bio': user_info.bio, 
                    'user_videos': user_videos,

                    
                    
                    })
            else: 
                profile_image = request.FILES.get('upload-new-profile-image')
                username = request.POST.get('username')
                bio = request.POST.get('bio')
                location = request.POST.get('location')
                denomination = request.POST.get('denomination')
                senior_pastor = request.POST.get('senior_pastor')
                founded_date = request.POST.get('founded_date')
                introductory_video = request.FILES.get('upload-intro-video')
                
                if profile_image:
                    user_info.profile_img = profile_image
                if username: 
                    user_info.user.username = username
                    user_info.user.save()
                if bio: 
                    user_info.bio = bio
                if denomination:
                    user_info.denomination = denomination
                if location: 
                    user_info.location = location
                if senior_pastor:
                    user_info.senior_pastor = senior_pastor
                if founded_date:
                    user_info.founded_date = founded_date
                if introductory_video:
                    user_info.introductory_video_file = introductory_video
                user_info.save()



                return render(request, 'church_profile.html', {
                    'username': user_info.user,
                    'profile_photo': user_info.profile_img,
                    'denomination': user_info.denomination,
                    'bio': user_info.bio, 
                    'founded_date': user_info.founded_date,
                    'introductory_video': user_info.introductory_video_file,
                    'location': user_info.location,
                    'senior_pastor': user_info.senior_pastor,
                    'user_videos': user_videos,


                })
    else: 
            if user_info.user_type == 'user':
                return render(request, 'user_profile.html', {        
                    'username': user_info.user,
                    'profile_photo': user_info.profile_img,
                    'base_church': user_info.home_church,
                    'denomination': user_info.denomination,
                    'bio': user_info.bio, 
                    'user_videos': user_videos,

                    
                    
                    })
            else: 

                return render(request, 'church_profile.html', {
                    'username': user_info.user,
                    'profile_photo': user_info.profile_img,
                    'denomination': user_info.denomination,
                    'bio': user_info.bio, 
                    'founded_date': user_info.founded_date,
                    'introductory_video': user_info.introductory_video_file,
                    'location': user_info.location,
                    'user_videos': user_videos,

                })


@login_required(login_url='login/')
def logout_user(request):
    logout(request)
    return redirect('/login')
    

@login_required(login_url='/user_login')
def create_content(request):

    if request.method == 'POST':
        

        video = request.FILES.get('video-upload')
        thumbnail = request.FILES.get('thumbnail-upload')
        title = request.POST.get('title')
        description = request.POST.get('description')
        username = request.user.username

        user_model = User.objects.get(username=username)
            
        new_profile = Video.objects.create(user=user_model, video_file=video, title=title, description=description, thumbnail=thumbnail)



        return redirect('/user_profile')

    else: 
        user_info = Profile.objects.get(user=request.user)

        return render(request, 'create_content.html', {

            'username': user_info.user.username,
            'profile_photo': user_info.profile_img
        } )
    
@login_required(login_url='login/')

def watch_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    user_info = Profile.objects.get(user=video.user)
    
    all_videos = Video.objects.all()


    return render(request, 'click_video.html', {
        'video': video,
        'username': user_info.user,
        'profile_img': user_info.profile_img,
        'all_videos': all_videos,
        })


def other_user_profile(request, username):
    user_info = get_object_or_404(Profile, user__username=username)
    user_videos = Video.objects.filter(user=username).order_by('date_published')
    if user_info.user_type == 'user':


        return render(request, 'user_profile.html', {        
            'username': user_info.user,
            'profile_photo': user_info.profile_img,
            'base_church': user_info.home_church,
            'denomination': user_info.denomination,
            'bio': user_info.bio, 
            'user_videos': user_videos,

            
            
            })
    else: 



        return render(request, 'church_profile.html', {
            'username': user_info.user,
            'profile_photo': user_info.profile_img,
            'denomination': user_info.denomination,
            'bio': user_info.bio, 
            'founded_date': user_info.founded_date,
            'introductory_video': user_info.introductory_video_file,
            'location': user_info.location,
            'senior_pastor': user_info.senior_pastor,
            'user_videos': user_videos,


        })

