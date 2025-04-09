from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Переопределенная модель пользователя."""
    
    bio = models.CharField('Биография', max_length=100)
