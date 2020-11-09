from django.db.models import *
from django.utils import timezone
from django.contrib.auth.models import User


class Posts(Model):
    general_description = CharField(max_length=250)
    is_completed = BooleanField()
    detailed_description = TextField(null=True),
    is_important = BooleanField()
    datetime_posted = DateTimeField(default=timezone.now)
    expertise = TextField()
    author = ForeignKey(User, on_delete=CASCADE)
    
    def __str__(self):
        return self.general_description


class Users(Model):
    name = TextField()
    email = TextField()
    is_super_user = BooleanField()
    user_group = TextField()

    def __str__(self):
        return self.name


class UserGroup(Model):
    group_details = TextField()

    def __str__(self):
        return self.group_details
