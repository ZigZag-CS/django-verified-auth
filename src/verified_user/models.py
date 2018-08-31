"""Abstract and Mixin classes to build a Verified User

No concrete model is provided in this package, forcing developers to
inherit this in a User model in their own project, providing best-case
long-term protection.

"""
from django.db.models import BooleanField, Model
from django.utils.translation import ugettext_lazy as _
from improved_user.model_mixins import AbstractUser as BaseUser


class VerifiedEmailBoolMixin(Model):
    """Provide boolean field to verify that email has been confirmed."""

    is_verified = BooleanField(_("email verified"), default=False)

    class Meta:
        abstract = True


class AbstractUser(VerifiedEmailBoolMixin, BaseUser):
    """Define base abstract user with new behaviors

    This is the recommended class to use when integrating this package.

    Provides:
        - a boolean field for email verification status

    """

    class Meta:
        abstract = True
