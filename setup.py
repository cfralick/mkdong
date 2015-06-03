#!/usr/bin/env python

import os
import sys

try:
    import setuptools
except ImportError as err:
    raise ImportError("It's your fault there's {}".format(err))

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from codecs import open

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


NAME = 'mkdong'

LICENSE = 'BSD-2-Clause'

AUTHOR = 'Clint Fralick'

AUTHOR_EMAIL = 'cfralick@creeperengine.com'

URL = 'https://bitbucket.org/cfralick/mkdong'

PACKAGES = find_packages(exclude=['docs', 'tests*'])

EXTRAS_REQUIRE = {'test': ['tox']}

CUSTOM_COMMANDS = {'test': Tox}

KEYWORDS = ('penis', 'dong', 'cli',)

CLASSIFIERS = (
    'Natural Language :: English',
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Programming Language :: Python',
)

ENTRY_POINTS = {
    'console_scripts': [
        'mkdong=mkdong.__main__:main'
    ]
}

with open(os.path.join(BASE_DIR, 'VERSION'), encoding='utf-8') as version:
    VERSION = version.read().strip()

with open(os.path.join(BASE_DIR, 'DESCRIPTION.rst'), encoding='utf-8') as descr:
    DESCRIPTION = descr.readline().strip()
    LONG_DESCRIPTION = descr.read()


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    keywords=KEYWORDS,
    url=URL,
    packages=PACKAGES,
    extras_require=EXTRAS_REQUIRE,
    cmdclass=CUSTOM_COMMANDS,
    classifiers=CLASSIFIERS,
    entry_points=ENTRY_POINTS
)
