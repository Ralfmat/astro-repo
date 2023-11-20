from django.contrib.auth.models import User
from django.db import models
from events.models import Event

class SavedEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
