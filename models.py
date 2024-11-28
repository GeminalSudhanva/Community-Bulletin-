from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.IntegerField()
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Standard', 'Standard'),
        ('Viewer', 'Viewer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Standard')

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Attachment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)

class Report(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
