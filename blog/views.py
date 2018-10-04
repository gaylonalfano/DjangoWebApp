from django.shortcuts import render
#from django.http import HttpResponse  - Can remove this once we start using/rendering templates instead
from .models import Post

'''
What if we wanted our pages to have images or posts by different authors, etc.? We want to display them in our templates. 
let’s add some dummy data into our blog > views.py and see how to pass that to our templates. Ex. posts which is a 
list of dictionaries, each dict is a post
'''
posts = [
    {
        'author': 'CoreyMS', 
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe', 
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
# Now, let's pretend we made a database call and got back this list of posts. We want to display 
# this list of posts on our blog homeplage. We can pass these posts into our template just by passing
# an argument with our data. We'll put our data into a dictionary within home() view (see below). 
# Then, we can pass that context as our third argument to our render function. By doing this, it will
# pass that data into our template and let us access it from within the template. 
# So now whatever key name we use in this dictionary that we passed in (i.e., 'posts') will be accessible
# from within the template, and it will be equal to that value. So we will have access to the 'posts' key variable
# which will be equal to the posts list of dictionaries containing information of each post. 
# **Head to home.html template so we can see how to use it.

# Create your views here.
def home(request):
    """Handle traffic from homepage of blog. Return what we want the user to see"""
    context = {
        'posts': Post.objects.all()
    }
    #return HttpResponse('<h1>Blog Home</h1>')  # Better is to use a template
    return render(request, 'blog/home.html', context)

# Next, need to map URL pattern to this view function just yet. Need to create
# a new module in our blog directory called URLS.py. In that file, we'll map the
# urls we want to correspond to each view function.

# After the blog home route, let's add another route to our blog - the About page
# first in views.py, we write a function that will handle the logic for the about page.
# After we define the about(), we need to edit blog.urls module to setup the mapping to 
# the path of our views.py about() function.
def about(request):
    """Handle how we want to handle the logic of the about page"""
    #return HttpResponse('<h1>Blog About</h1>')
    # Can pass dict directly if not too large {'title': ...}
    return render(request, 'blog/about.html', {'title': 'About'})