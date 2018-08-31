"""Module to provide concrete user model for testing"""
from verified_user.models import AbstractUser


class User(AbstractUser):
    """User Model with verified email field"""
