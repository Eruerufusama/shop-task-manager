from django.db.models import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse





class UserGroup(Model):
    group_details = TextField()

    def __str__(self):
        return self.group_details

        
class Posts(Model):
    general_description = CharField(max_length=250)
    is_completed = BooleanField()
    is_important = BooleanField()
    datetime_posted = DateTimeField(default=timezone.now)
    expertise = ForeignKey(UserGroup, on_delete=CASCADE)
    author = ForeignKey(User, on_delete=CASCADE)
    is_inprogress = BooleanField(null=True)

    def __str__(self):
        return self.general_description
    
    def get_absolute_url(self):
        return reverse('posts-detail', kwargs={'pk':self.pk})


