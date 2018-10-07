from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

    # This is the method that gets run after the model 
    def save(self):
        super().save()  # the parent class save() would run when we save an instance of profile
        # Now, we're going to grab the image that was saved and resize it using Pillow:
        # To open the image of the CURRENT profile instance do:
        img = Image.open(self.image.path)  
        # Next, want to specify what size we want the file to be. But first, let's check
        # if the current image is less than 300 pixels:
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)  
            img.thumbnail(output_size)  # resizes image
            img.save(self.image.path)  # save it back to same path to overwrite larger image