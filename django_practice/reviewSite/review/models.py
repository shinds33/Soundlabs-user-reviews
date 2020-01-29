from django.db import models
from django.utils import timezone

# Create your models here.

# CharField function must have a limit for the characters used
# TextField does not have a limit

class Comment(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)

