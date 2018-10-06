from django.db import models
from django.contrib.auth.models import User

'''
The default User model that Django provides for us doesn’t have a 
field for a profile pic, so how can we add the profile field? In order 
to do this, we’re going to have to extend the User model and create a 
new model that has a one-to-one relationship with the User. Meaning, one 
user can have one profile and one profile will be associated with one user. 
Let’s add this so that our users can have profile pictures. This will be 
a new model in our users app. When we created the users app, it created a 
models.py file for us. Let’s open it up.

We need to import the existing User model that Django provides.
'''

class Profile(models.Model):
    # Now create one-to-one relationship w/ existing User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Now that we have a user associated with this profile, we can add any fields
    # Note that the upload_to param will create
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"  # gaylonalfano Profile