from django.contrib import admin
from .models import Post

# Register your models here.
# Need to register our new Post model so that it shows up in admin page
admin.site.register(Post)
