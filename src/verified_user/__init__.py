"""Django Verified User

The Problem
-----------

Django expects User.is_active to be set to True when a user verifies
their email after registration. To disable the account, User.is_active
can be set to False.

How do we know the difference between users that have verified their
emails and users that have asked to disable their account, or else have
been banned? If our system allows for activation emails to be re-sent in
the event of lost-emails, how can we prevent banned accounts from
reactivating?

The Solution
------------

This package uses is_active to specify *only* whether a user may log in
or not. It creates a set of new fields to specify whether an email has
been verified, and whether account-reactivation is allowed. It
furthermore allows for a setting that defines whether or not email
verification is necessary before allowing the user to use the
application.

For more information, please see the documentation.

"""
