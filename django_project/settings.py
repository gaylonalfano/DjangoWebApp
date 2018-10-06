"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*e(14#3#a4&#t381q!)+m(=601%*s5q3n9^lx5rps(nvkmx4&&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
'''
Then we copy the ‘BlogConfig’ name, open the projects settings.py file where we need to add 
the path to this class within the installed apps list. Ex. Django_project > settings.py > 
INSTALLED_APPS = […, ‘blog.apps.BlogConfig’,…]. **This is needed every time you add a new application. 
You need this in order for Django to correctly search your templates and where Django looks for our 
models when working with databases. 

Next, let’s use that template we created so that it renders that whenever we navigate to our homepage. 
We have to point our blog views to use those templates. Need to open up blog >> views.py. Best way to 
load a template in the Django.shortcuts module: from django.shortcuts import render. **See views.py
'''
INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# Changing the default location for where images are saved. For performance reasons, 
# we want the files to be stored on the file system and not in the database. We also 
# don't want to clutter up the root directory with different image directories.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # the full path where we want Django to store uploaded files
MEDIA_URL = "/media/"  # this is the public URL of the MEDIA_ROOT dir!

# Tell Crispy Forms which CSS Framework to use
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# By default on the login page, Django will try to direct the user (after logging in)
# to the account profile page. We can change that to direct to the home page instead by 
# adding the following setting:
LOGIN_REDIRECT_URL = 'blog-home'

# After using @login_required to the profile view, Django by default will try to direct
# users (not logged in) to /accounts/login/?next=/profile/. We want to change it to our /login
# view that we've already created/setup. 'login' is the name that we gave to our urlpattern in 
# our login route:
LOGIN_URL = 'login'