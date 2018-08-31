"""Test model attributes and behavior for Verified User"""
from improved_user.model_mixins import AbstractUser
from pytest import mark

from .models import User


def test_inheritance():
    """Does User inherit from AbstractUser?"""
    assert issubclass(User, AbstractUser)


@mark.django_db
def test_new_unverified_user():
    """Can we create a new unverified user?"""
    user = User.objects.create()
    assert user.is_verified is False


@mark.django_db
def test_new_verified_user():
    """Can we create a new verified user?"""
    user = User.objects.create(is_verified=True)
    assert user.is_verified is True
