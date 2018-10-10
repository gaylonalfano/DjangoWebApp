from django.shortcuts import render
#from django.http import HttpResponse  - Can remove this once we start using/rendering templates instead
from .models import Post
# Importing a class-based ListView then create a class:
# Importing a class-based DetailView then create a class:
# Importing a class-based CreateView then create a class:
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
# Need to make it if we try to access a create post detail page without being logged in,
# then should be redirected to the login page first. For class-based views we can't use the
# @login_required decorator like function-based views. Therefore, need to inherit from a 
# Login Mixin class then add/inherit this class into our classes below:
from django.contrib.auth.mixins import LoginRequiredMixin

'''
What if we wanted our pages to have images or posts by different authors, etc.? We want to display them in our templates. 
let’s add some dummy data into our blog > views.py and see how to pass that to our templates. Ex. posts which is a 
list of dictionaries, each dict is a post. 

After setting up a database to store data, you can update this views.py file to have context query the database
for all posts using: Post.objects.all(). Once you confirm that it's now pulling post data from the database,
you can delete (commented out) the dummy posts data (see below).
'''
# posts = [
#     {
#         'author': 'CoreyMS', 
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe', 
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]
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


# Section 10 - Creating a class since we're going to see the difference 
# between a class-based view (PostListView) and a function-based view (home):
class PostListView(ListView):
    # Need to create a variable called model. model will tell our ListView 
    # what model to query in order to create the list (all of our posts):
    model = Post
    # Changing which template we want this PostListView to look for:
    template_name = 'blog/home.html'  # Default is <app>/<model>_<viewtype>.html
    # Adding template_name won't work just yet because it doesn't know the variable name
    # in our template that we're going to be looping over (default is object_list but we used
    # 'posts' above in our home function view). Since we already have the template,
    # we'll set this variable/attribute here in this PostListView and that should do it:
    context_object_name = 'posts'
    # Adding an ordering attribute so have most recent posts up at the top of blog:
    ordering = ['-date_posted']

# Creating another class-based view that uses all the default naming conventions:
class PostDetailView(DetailView):
    model = Post

# Creating a Create view. It's a form where we create a new post, so let's add some fields:
# After we create this class/view, we need to update our url patterns with this new view.
# Need to inherit LoginRequiredMixin class to redirect users to login page if they try to view
# a create post detail page if not logged in. NOTE that you MUST inherit this on the FAR LEFT!:
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # overriding the form_valid() method:
    def form_valid(self, form):
        # Before submitting the form, take the instance and set the author equal to current user
        form.instance.author = self.request.user
        # After setting author to current user, return the form:
        return super().form_valid(form)

# Now creating an UpdateView
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # overriding the form_valid() method:
    def form_valid(self, form):
        # Before submitting the form, take the instance and set the author equal to current user
        form.instance.author = self.request.user
        # After setting author to current user, return the form:
        return super().form_valid(form)


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