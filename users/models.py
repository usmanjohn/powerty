from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from storages.backends.s3boto3 import S3Boto3Storage
from django.contrib.auth.models import AbstractUser
from topics.models import Topic, Answer
from django.db.models import Count, Q

class S3Storage(S3Boto3Storage):
    location = 'media'
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    
    is_member = models.BooleanField(default=False)
    image = models.ImageField(storage=S3Storage(),upload_to='profile_pics', default='profile_pics/default.jpg')
    bio = models.CharField(max_length=2000, default='I did not write a bio yet')
    date = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=15, unique=True)
    

    def __str__(self) -> str:
        return f'{self.user.username} Profile' 
    
   