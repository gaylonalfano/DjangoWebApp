# Creating this file so that we can add new fields to our UserCreationForm (eg email address,etc.)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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