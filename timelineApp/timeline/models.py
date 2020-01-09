from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50, default="Event")
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published', default="2020-01-01 06:00")
    image = models.ImageField(upload_to='media/', default="")

    def __str__(self):
        return self.title

class Timeline(models.Model):
    title = models.CharField(max_length=50, default="New Timeline")
    events = models.ForeignKey(Event, on_delete=models.CASCADE)
    tagged_users = models.IntegerField(default=0)
    pub_date = models.DateTimeField('Date published', default="2020-01-01 06:00")

    def __str__(self):
        return self.title