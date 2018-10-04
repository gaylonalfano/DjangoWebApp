# We need to think about what we actually want to save to the DB. We're going to have
# users (authors of the posts) and the posts themselves. We already know how to create 
# users in the admin. For now, we're just going make a post model. This will be a class
# that inherits from django models class. 

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Let's create our post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

