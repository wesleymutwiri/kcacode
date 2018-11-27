from django.db import models
import datetime as dt 
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    date =  models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    profile_avatar = ProcessedImageField(upload_to = 'avatars/', processors=[ResizeToFill(100,100)], format = 'JPEG', options ={'quality':60})

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(username=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def save_profile(self):
    self.save()

def delete_profile(self):
    self.delete()

class Feedback(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=255)
    date =  models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete= models.CASCADE )
    
    class Meta:
        ordering = ['date']

    @classmethod
    def get_all_feedback(cls):
        feedback = cls.objects.order_by(date)
        return feedback

    def save_feedback(self):
        self.save()

class Report(models.Model):
	body = models.TextField()
	title = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
    # feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
	

     