from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    """Handle traffic from homepage of blog. Return what we want the user to see"""
    return HttpResponse('<h1>Blog Home</h1>')

# Next, need to map URL pattern to this view function just yet. Need to create
# a new module in our blog directory called URLS.py. In that file, we'll map the
# urls we want to correspond to each view function.

# After the blog home route, let's add another route to our blog - the About page
# first in views.py, we write a function that will handle the logic for the about page.
# After we define the about(), we need to edit blog.urls module to setup the mapping to 
# the path of our views.py about() function.
def about(request):
    """Handle how we want to handle the logic of the about page"""
    return HttpResponse('<h1>Blog About</h1>')