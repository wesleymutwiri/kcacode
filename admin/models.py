from django.db import models
import datetime as dt 
from django.dispatch import receiver
from django.db.models.signals import post_save# Create your models here.

class Report(models.Model):
	body = models.TextField()
	title = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)

class 