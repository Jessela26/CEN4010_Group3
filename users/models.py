from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):#associating User model with Profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)#if profile is deleted, do not delete the user

    def __str__(self):
        return f'{self.user.username} Profile'


