# Use signals to automatically create a profile for each new user
# and give them the default profile image
from django.db.models.signals import post_save

# The User model is going to be the SENDER (i.e., it's sending the signal)
from django.contrib.auth.models import User

# We also going to need to create a receiver, which is a function 
# that gets some signal and then performs some task.
from django.dispatch import receiver

# We want to import Profile from our models
from .models import Profile

# Write a function that creates a user profile for each new user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # if User created, then create 
        # Profile obj w/ user= the instance of User that was created

        # Now we have to tie the functionality together (create new user 
        # auto create user profile). To do this, we're going to use that 
        # receiver we imported and it's going to be a decorator

# Create a function that saves our profile every time the User object gets saved
@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()  # instance is the User. Save profile when user is saved.