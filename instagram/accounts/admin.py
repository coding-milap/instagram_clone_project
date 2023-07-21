from django.contrib import admin
from .models import User
from .models import UserToUserLink,UserPost,FollowRequest

# # Register your models here.
admin.site.register(User)
admin.site.register(UserPost)
# admin.site.register(Like)
# admin.site.register(Comment)
admin.site.register(UserToUserLink)
admin.site.register(FollowRequest)