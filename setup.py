#!/usr/bin/env python3
"""Django Verified Auth

:website: https://github.com/jambonsw/django-verified-auth
:copyright: Copyright 2018 JamBon Software
:license: Simplified BSD, see LICENSE for details.

"""
from distutils.command.check import check as checkcommand
from os.path import abspath, dirname, join

from setuptools import find_packages, setup

HERE = abspath(dirname(__file__))


def load_file_contents(file_path, as_list=False):
    """Load file as string or list"""
    abs_file_path = join(HERE, file_path)
    with open(abs_file_path, encoding="utf-8") as file_pointer:
        if as_list:
            return file_pointer.read().splitlines()
        return file_pointer.read()


LONG_DESCRIPTION = (
    load_file_contents("README.rst")
    .split(".. end-badges")[1]  # remove badge icons at top
    .lstrip()  # remove any extraneous spaces before title
)


class CustomCheckCommand(checkcommand):
    """Customize distutils check command"""

    # https://github.com/python/cpython/blob/master/Lib/distutils/command/check.py
    user_options = checkcommand.user_options + [
        ("disable-metadata", None, "don't check meta-data"),
        ("enforce-email", "e", "Ensure that all author/maintainer use email"),
    ]
    negative_opt = {"disable-metadata": "metadata"}

    def initialize_options(self):
        """Set new options"""
        super().initialize_options()
        self.enforce_email = 0

    def check_metadata(self):
        """Ensure that all required elements of meta-data are supplied.

        Specifically: name, version, URL, author or maintainer
        Warns if any are missing.

        If enforce-email option is true, author and/or maintainer must
        specify an email.

        """
        metadata = self.distribution.metadata

        missing = []
        for attr in ("name", "version", "url"):
            if not (hasattr(metadata, attr) and getattr(metadata, attr)):
                missing.append(attr)

        # https://www.python.org/dev/peps/pep-0345/
        # author or maintainer must be specified
        # author is preferred; if identifcal, specify only author
        if not metadata.author and not metadata.maintainer:
            missing.append("author")
            if self.enforce_email:
                missing.append("author_email")
        else:
            # one or both of author or maintainer specified
            if (
                metadata.author
                and self.enforce_email
                and not metadata.author_email
            ):
                missing.append("author_email")
            if (
                metadata.maintainer
                and self.enforce_email
                and not metadata.maintainer_email
            ):
                missing.append("maintainer_email")
            if (
                metadata.author
                and metadata.maintainer
                and metadata.author == metadata.maintainer
            ):
                self.warn(
                    "Maintainer should be omitted if identical to Author.\n"
                    "See https://www.python.org/dev/peps/pep-0345/"
                    "#maintainer-email-optional"
                )
            if (
                metadata.author_email
                and metadata.maintainer_email
                and metadata.author_email == metadata.maintainer_email
            ):
                self.warn(
                    "Maintainer Email should be omitted if"
                    "identical to Author's.\n"
                    "See https://www.python.org/dev/peps/pep-0345/"
                    "#maintainer-email-optional"
                )

        if missing:
            self.warn("missing required meta-data: %s" % ", ".join(missing))


setup(
    name="django-verified-auth",
    version="0.0.1",
    description=("Django app to explicitly handle user email verification"),
    long_description=LONG_DESCRIPTION,
    url="https://github.com/jambonsw/django-verified-auth",
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=["pytest-runner"],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-django",
        "pytest-emoji",
        "coverage>=4,<5",
    ],
    install_requires=[
        "django>=2.1",
        "django-improved-user>=1.0",
        "pytz>=2018.5",
    ],
    extras_require={
        "factory": ["factory_boy>=2.9", "Faker>=0.8", "python-dateutil>=2.6"]
    },
    cmdclass={"check": CustomCheckCommand},
    zip_safe=False,
    author="Andrew Pinkham",
    license="BSD License",
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Framework :: Django",
        "Framework :: Django :: 2.1",
    ],
)
