from django.apps import AppConfig

'''
In the home.html, we have to add our blog application to our list of installed apps so that django 
knows to look there for a templates directory. To add our application to the list, it’s recommended 
we add our app configuration to our project’s settings.py module. Our app configuration is location 
inside our apps.py module within our application (ex. within blog application we should have an apps.py 
module and we can see a class BlogConfig(AppConfig).
'''
class BlogConfig(AppConfig):
    name = 'blog'
