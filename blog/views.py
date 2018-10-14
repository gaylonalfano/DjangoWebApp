# Return 404 if the user doesn't exist for UserPostListView using get_object_or_404
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse  - Can remove this once we start using/rendering templates instead
from .models import Post
# Importing User so we can grab user for only displaying posts by that user:
from django.contrib.auth.models import User
# Importing a class-based ListView then create a class:
# Importing a class-based DetailView then create a class:
# Importing a class-based CreateView then create a class:
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Need to make it if we try to access a create post detail page without being logged in,
# then should be redirected to the login page first. For class-based views we can't use the
# @login_required decorator like function-based views. Therefore, need to inherit from a 
# Login Mixin class then add/inherit this class into our classes below:
# To restrict users from editing other users' posts, import UserPassesTestMixin:
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    # Adding pagination. With class-based views, don't need to import Paginator class
    # Instead, just need to set the paginate_by = (number of posts per page) attribute:
    paginate_by = 5  # we'll set it like 5 or 10 posts per page later

# Create a route that will display only the posts from a particular user when you click their link.
# If the user has lots of posts, paginate those posts as well. Similar to PostListView so copy:
class UserPostListView(ListView):
    # Need to create a variable called model. model will tell our ListView 
    # what model to query in order to create the list (all of our posts):
    model = Post
    # Changing which template we want this PostListView to look for:
    template_name = 'blog/user_posts.html'  # Default is <app>/<model>_<viewtype>.html
    # Currently this will still list all the posts from our Post model. However, we want
    # to add a filter to this so that only it gets the posts from a certain user. This will
    # come directly from the URL. So, when we create a new URL pattern for this, we'll specify
    # the username and the URL path itself. So we'll set that when we create the URL pattern in'
    # a second, but for now let's just assume that we have a username variable passed into the URL.
    # In order to modify the query set that this ListView returns, we can override a method 
    # called get_query_set and change the query set from within there.

    # we'll set this variable/attribute here in this UserPostListView and that should do it:
    context_object_name = 'posts'
    # Adding pagination. With class-based views, don't need to import Paginator class
    # Instead, just need to set the paginate_by = (number of posts per page) attribute:
    paginate_by = 5  # we'll set it like 5 or 10 posts per page later

    # Overriding get_query_set function to modify what the ListView query returns:
    def get_query_set(self):
        # Get the user associated with the username that we're going to get from the URL
        # if the user exists we'll capture them in the user variable. 
        # if the user doesn't exist then return 404 telling them the user doesn't exist.
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # Limit the results of query and order by desc date posted:
        return Post.objects.filter(author=user).order_by('-date_posted')


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
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # overriding the form_valid() method:
    def form_valid(self, form):
        # Before submitting the form, take the instance and set the author equal to current user
        form.instance.author = self.request.user
        # After setting author to current user, return the form:
        return super().form_valid(form)

    # Creating a function to restrict users from updating other users' posts
    # Need to use UserPassesTestMixin so need to inherit that class within PostUpdateView:
    def test_func(self):
        # Retrieve the exact post that we're updating:
        post = self.get_object()
        # Check if user is the author of the current post:
        if self.request.user == post.author:
            return True
        return False


# Creating a PostDeleteView for deleting posts. Need to import the Mixins to 
# ensure that the user is logged in and is the actual author of the post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # In order to delete a post, it needs a success_url to know where to redirect:
    success_url = '/' # '/' is the homepage
    # Creating a function to restrict users from updating other users' posts
    # Need to use UserPassesTestMixin so need to inherit that class within PostUpdateView:
    def test_func(self):
        # Retrieve the exact post that we're updating:
        post = self.get_object()
        # Check if user is the author of the current post:
        if self.request.user == post.author:
            return True
        return False

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