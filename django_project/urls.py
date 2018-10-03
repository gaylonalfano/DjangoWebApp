"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# We have one route to our admin. Now we're going to tell django which route
# should get mapped to our blog urls. Need to import the include function from 
# django.urls (see above).

# if we were developing a new version of blog, could just add a 'blog_dev/' path
# and then it applies to all the connected routes.

# The "/" is good because by default if it has a "/", then Django will redirect routes w/o a "/"
# to that route that has one. Ex. So 'blog_dev' and 'blog_dev/' will get redirected to blog/ routes.

# What if we wanted our blog to be the home page of our entire website? We can just simply leave the 
# path to our blog empty '': path('', include('blog.urls'))
# By doing that it will match the empty path to our project urls and our blog urls and return the home page.
# Leaving it this way but could always add a non-empty path to our urlpatterns:  path('blog/', include('blog.urls'))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))  # if we go to /blog, we should now reference/send users to our blog.urls
    # When Django encounters include(), it chops off the included portion of the url ("/blog") and only sends the
    # remaining string to the included blog.urls module to get processed. Since nothing remainining, it just sends empty
    # string ''. Now over to blog.urls...
]
