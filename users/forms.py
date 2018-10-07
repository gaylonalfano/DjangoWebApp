# Creating this file so that we can add new fields to our UserCreationForm (eg email address,etc.)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# import Profile model so we can work/edit profile pictures in the ProfileUpdateForm
from .models import Profile

# Create a new form/new class that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # add additional fields we want
    email = forms.EmailField(required=True)

    # Within Meta we're going to describe the model that we want this form to interact with
    # Whenever this form validates it's going to create a new User
    # Meta gives us a nested namespace for configurations
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# We're going to create a model form. This form allows us to create a form that will work
# with a specific database model. In this case we want a form that will update our User model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # adding the additional email field to the form

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']