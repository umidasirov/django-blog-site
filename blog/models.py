from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

class Users(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    job = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.surname}"

from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # yangi maydon
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
