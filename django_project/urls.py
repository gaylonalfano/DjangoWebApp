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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

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

# After learning about forms and using Django's UserCreationForm, we could either create a separate urls.py 
# module for our users app (like we did for blog app), but Corey had us hold off. So instead we're going to import
# our view (register() in views.py) directly into our projects urls module (here).

# We've completed the registration page but now we need to allow users to actually login.
# Django has some default login and logout views so let's import them into this urls.py module
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', include('blog.urls')),  # if we go to /blog, we should now reference/send users to our blog.urls
    # When Django encounters include(), it chops off the included portion of the url ("/blog") and only sends the
    # remaining string to the included blog.urls module to get processed. Since nothing remainining, it just sends empty
    # string ''. Now over to blog.urls...

    # After import django's default user login/logout views, time to create paths for them:
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # Creating a route that provides a form for our user to fill out that will email reset password instructions:
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),

    # After creating a user profile view and the users/profile.html template, let's create a route to use this view:
    path('profile/', user_views.profile, name='profile')

]

# Modified to be more explicit. Helps others who are reading our code. We're only adding this on when 
# we're in DEBUG mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Original snippet from django's docs for media: 
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)