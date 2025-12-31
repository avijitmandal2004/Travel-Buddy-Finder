from django.contrib.auth.models import User
from django.db import models

class BuddyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    languages = models.CharField(max_length=200)
    interests = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username


class Trip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.PositiveIntegerField()
    looking_for = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.destination} ({self.owner.username})"

