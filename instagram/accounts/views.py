from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import User,UserToUserLink,UserPost,FollowRequest
from django.contrib.auth import login,logout,authenticate
from django.db.models import Q 
from datetime import datetime
import random
from django.contrib import messages
# Create your views here.


def user_register(request):

    if request.method == "POST":

        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:

            return HttpResponseRedirect(reverse('user-register'))
        
        user = User.objects.create(email=email,first_name=first_name,last_name=last_name,username=username)
        user.set_password(password1)
        user.save()

        return HttpResponseRedirect(reverse('user-login'))

        


    return render(request,'accounts/user-register.html')

def user_login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email,password=password)

        if user:

            login(request,user)

            return HttpResponseRedirect(reverse('home'))

    return render(request,'accounts/user-login.html')

def user_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('user-login'))

# Displays Latest Posts First which are posted by Following and also displays suggestion of users to follow.
def home(request):

    users = User.objects.exclude(email=request.user)
    length = len(users)
    connection = UserToUserLink.objects.filter(Q(user1=request.user,is_follow=True))
    following = []
    for conn in connection:

        following.append(conn.user2.email)
    
    all_posts = UserPost.objects.exclude(user_posted=request.user).order_by('-created_at')
    try:
        random_num1 = random.randint(0,length)
        random_num2 = random_num1 + 5
        users = users[random_num1:random_num2]
    except:

        users = users[0:5]
    

    print(users)
    

    return render(request,'accounts/index.html',{'all_posts':all_posts,'following':following,'users':users})


def send_follow_request(request,user2):

    messages.success(request, "Follow Request has been Sent...")

    user1 = request.user
    user2 = User.objects.get(pk=user2)

    notification = FollowRequest(follower=user1,following=user2)
    notification.save()

    return HttpResponseRedirect(reverse('home'))

def show_follow_request(request):

    follow_requests = FollowRequest.objects.filter(following=request.user)

    return render(request,'accounts/follow_requests.html',{'follow_requests':follow_requests})

def accept_follow_request(request,user1):

    user1 = User.objects.get(pk=user1)
    user2 = request.user

    follow_request = FollowRequest.objects.filter(Q(follower=user1) and Q(following=user2))[0]
    follow_request.is_accepted = True
    follow_request.save()

    user_to_user_link = UserToUserLink.objects.create(user1=user1,user2=user2,is_follow=True)
    user_to_user_link.save()
    
    return HttpResponseRedirect(reverse('show-follow-requests'))


def profilePage(request):
    user = request.user
    posts = UserPost.objects.filter(user_posted=request.user)

    return render(request,'accounts/user-profile.html',{'posts':posts,'user':user})
























# def user_profile(request,username):
#     print(username)
#     user = User.objects.filter(username=username)
#     print(user)
#     user = user[0]

#     return render(request,'accounts/user-profile.html',{'user':user})


# def send_follow_request(request,user):

#     user1 = request.user
#     user2 = User.objects.get(pk=user)
#     print(user1.username,user2.username)

#     notification = Notifications.objects.create(user1=user1,user2=user2)

#     return HttpResponseRedirect(reverse('home'))

# def show_follow_requests(request):

#     notifications = Notifications.objects.filter(user2=request.user)

#     return render(request,"accounts/notifications.html",{'notifications':notifications})


# def accept_follow_requests(request,user):

#    user1 = User.objects.get(pk=user)
#    user1.following = user1.following + 1
#    user1.save()
#    user2 = request.user
#    user2.followers = user2.followers + 1
#    user2.save()
   
#    notification  = Notifications.objects.filter(user1=user,user2=user)
#    notification = notification[0]
#    notification.is_accepted = True
#    notification.save()
#    return  HttpResponseRedirect(reverse('notifications'))
