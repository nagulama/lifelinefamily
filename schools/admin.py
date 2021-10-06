from django.contrib import admin
from .models import File, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(File)