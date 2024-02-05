from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_CATEGORIES = [
        ('student', 'Student'),
        ('entreprise', 'Entreprise'),
    ]

    category = models.CharField(max_length=20, choices=USER_CATEGORIES, default='student')


