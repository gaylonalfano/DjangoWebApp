from django.contrib import admin
from .models import Profile

# Register your models here.
# Register this model within our admin.py file of our users 
# app in order To view these user profiles on the admin page of our website.
# We want to register the profile model we just created
admin.site.register(Profile)

