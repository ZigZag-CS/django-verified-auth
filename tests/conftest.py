"""Global configuration/fixture functions for pytest"""
from django.conf import settings

###############################################################################
#                           General Django Fixtures                           #
###############################################################################


def pytest_configure():
    """Configure pytest with Django settings"""
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.sites",
            "tests",
        ],
        SITE_ID=1,
        MIDDLEWARE=[
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
        ],
    )


###############################################################################
#                         PyTest Emoji Configuration                          #
###############################################################################


def pytest_emoji_passed(config):  # pylint: disable=unused-argument
    """Shown when a test passes"""
    return "✅ ", "✅ Passed "


def pytest_emoji_failed(config):  # pylint: disable=unused-argument
    """Shown when a test fails"""
    return "❌ ", "❌ Failed "


def pytest_emoji_skipped(config):  # pylint: disable=unused-argument
    """Shown when a test is skipped"""
    return "🙈 ", "🙈 Skipped "


def pytest_emoji_error(config):  # pylint: disable=unused-argument
    """Shown when an unexpected error is raised"""
    return "⚠️️ ", "⚠️ Error "


def pytest_emoji_xfailed(config):  # pylint: disable=unused-argument
    """Shown when a test fails expectedly."""
    return "❎", "❎ Expected Failure "


def pytest_emoji_xpassed(config):  # pylint: disable=unused-argument
    """Shown when an expected failure actually passes."""
    return "😱 ", "😱 Unexpected Pass"
