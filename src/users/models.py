from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Расширение модели пользователя, сделал поле email уникальным.
    """
    email = models.EmailField(max_length=100, unique=True)
