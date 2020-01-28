from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    reward_points = models.IntegerField(blank=False, default=0) 