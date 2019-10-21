from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# each class is it's own table in the DB
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted we want to delete their posts as well