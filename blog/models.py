# We need to think about what we actually want to save to the DB. We're going to have
# users (authors of the posts) and the posts themselves. We already know how to create 
# users in the admin. For now, we're just going make a post model. This will be a class
# that inherits from django models class. 

# After making changes, need to run python manage.py makemigrations to update any changes
# to the database.  # blog/migrations/0001_initial.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Want to get/return the URL as a string to the view so need to import reverse. 
# The view will handle the redirect for us:
from django.urls import reverse

# Let's create our post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Without this __str__ method, the print out for Post.objects.all()
    # is really basic. This results in:  <QuerySet [<Post: Blog 1>]>
    def __str__(self):
        return self.title

    # Need to create the get_absolute_url method so Django can find the location to a specific post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})