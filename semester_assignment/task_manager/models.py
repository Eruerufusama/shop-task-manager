from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


class Posts(models.Model):
    general_description = models.CharField(max_length=250)
    is_completed = models.BooleanField()
    detailed_description = models.TextField(null=True),
    is_important = models.BooleanField()
    datetime_posted = models.DateTimeField(default=timezone.now)
    expertise = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.general_description

class Users(models.Model):
    name = models.TextField()
    email = models.TextField()
    is_super_user = models.BooleanField()
    user_group = models.TextField()

    def __str__(self):
        return self.name



class UserGroup(models.Model):
    group_details = models.TextField()
    


    def __str__(self):
        return self.group_details
