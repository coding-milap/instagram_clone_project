from django.urls import path
from . import views

urlpatterns = [

    path('feed',views.home,name="home"),
    path('user-register',views.user_register,name="user-register"),
    path('user-login',views.user_login,name="user-login"),
    path('user-logout',views.user_logout,name="user-logout"),
    path('send-follow-request/<str:user2>',views.send_follow_request,name="send-follow-request"),
    path('show-follow-requests',views.show_follow_request,name="show-follow-requests"),
    path('accept-follow-request/<str:user1>',views.accept_follow_request,name="accept-follow-request"),
    path('user-profile',views.profilePage,name="user-profile"),
 ]
