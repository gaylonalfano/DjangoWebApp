from django.urls import path
from . import views  # "." means current directory

# Now let's create a path to our blog home page
# views.home will return the HTTP response that we're on the blog page.
# Used "blog-home" instead of just "home" because there are times we will want to do a reverse
# lookup on this route, naming it just "home" could collide with other app routes (store app, etc.).
# Doesn't work just yet because the main urls module. It tells us which urls will send us to our blog app.

# Continuing after the django_project.urls: The include() only sends the remaining string to this blog.urls module.
# Next, since nothing remaining (empty ''), it looks for '' pattern here and finds it (below). That '' pattern
# will be handled by the function, views.home. So then we can navigate to views.py file and to the home(), which
# just returns a HttpResponse h1 tag with Blog-Home.

# Next route: About page
urlpatterns = [
    path('', views.home, name="blog-home"),  
    path('about/', views.about, name="blog-about")  # Don't need to add anything to project.urls patterns since we're still under /blog
]