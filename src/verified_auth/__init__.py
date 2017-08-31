"""Django app to explicitly handle user email verification

The app provides User and Profile models. Both of these may be used
directly, but their Abstract counterparts may also be extended for full
customization. Please note that Profile is a swappable model.

The app furthermore provides an Authentication Backend that optionally
rejects users if their email is unverified.

Finally, the app provides a full suite of URLs and views to help
register and deactivate users.
"""
