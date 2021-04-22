from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    biography = models.TextField()
    contacts = models.CharField(max_length=255)
    edit_ip = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

