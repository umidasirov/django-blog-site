from django.contrib import admin
from .models import User,Profile,Post
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)