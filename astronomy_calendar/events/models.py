from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    followers = models.IntegerField()

    def __str__(self):
        return self.event_name