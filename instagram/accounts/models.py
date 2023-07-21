from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser
import uuid
# Create your models here.


class UserManager(BaseUserManager):


    def create_user(self,email,password,**extra_fields):

        if not email:

            return ValueError("Email must be there")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(self.db)

        return user
    
    def create_superuser(self,email,password,**extra_fields):

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:

            raise ValueError(("Super user must have is_staff True. "))

        return self.create_user(email,password,**extra_fields)



class User(AbstractUser):

    GENDER = (('Male','Male'),('Female','Female'),('Custom','Custom'),('Prefer not to say','Prefer not to say'))

    username = models.CharField(max_length=30)
    email = models.CharField(max_length=60,primary_key=True)
    phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="userPics",default="../static/accounts/images/Background-image.jpg")
    Bio = models.CharField(max_length=150)
    link = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER,max_length=20)
    followers = models.BigIntegerField(default=0)
    following = models.BigIntegerField(default=0)
    posts = models.BigIntegerField(default=0)
    story = models.FileField(upload_to="stories",default="../static/accounts/images/Background-image.jpg")
    is_private = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):

        return self.email


class UserPost(models.Model):

    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    user_posted = models.ForeignKey(User,on_delete=models.CASCADE,related_name="userposts")
    caption = models.CharField(max_length=100)
    location=models.CharField(max_length=150)
    post = models.FileField(default="",upload_to="userposts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user_posted.email


class UserToUserLink(models.Model):

    user1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user1")
    user2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user2")
    is_follow = models.BooleanField(default=False)


    def __str__(self) :

        return f"{self.is_follow}"


class FollowRequest(models.Model):

    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name="followerFollow")
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name="followingFollow")
    is_accepted = models.BooleanField(default=False)

    def __str__(self):

        if self.is_accepted:

            return f"{self.follower} follows {self.following}"
        else:

            return f"{self.follower} send a follow request to {self.following}"

# class Stories(models.Model):

#     story_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_stories")
#     story = models.FileField(default="",upload_to="stories")
    

#     def __str__(self):

#         return f"Story is posted by {self.user.first_name}"



    


















































# class Like(models.Model):

#     like_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)
#     count = models.BigIntegerField(default=0)
#     liked_by = models.OneToOneField(User,on_delete=models.CASCADE)

#     def __str__(self):

#         return f"{self.count}"

# class Comment(models.Model):

#     comment_id = models.UUIDField(default=uuid.uuid4,primary_key=True),
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)
#     count = models.BigIntegerField(default=0)
#     body = models.TextField()
#     commented_by = models.OneToOneField(User,on_delete=models.CASCADE)

#     def __str__(self):

#         return self.body