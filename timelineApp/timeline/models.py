from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Timeline(models.Model):
    title = models.CharField(max_length=50, default="New Timeline")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # events = models.ManyToOneRel(Event, on_delete=models.CASCADE)
    tagged_users = models.IntegerField(default=0)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    #timeline_id = models.ForeignKey(Timeline, default=0)

    def __str__(self):
        return self.title
    

class Event(models.Model):
    title = models.CharField(max_length=50, default="Event")
    description = models.CharField(max_length=200)
    date = models.DateTimeField('Date', default=timezone.now)
    image = models.ImageField(upload_to='media/', default="")
    timeline_id = models.ForeignKey(Timeline, on_delete=models.CASCADE, default=0)
    
    def __str__(self):
        return self.title