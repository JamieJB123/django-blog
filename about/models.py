from django.db import models
# User Model
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name="about_entry")

    def __str__(self):
        return self.title
