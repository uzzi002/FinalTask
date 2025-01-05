from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    """Represents an event with title, description, date, location, and organizer."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the title of the event as its string representation."""
        return self.title
