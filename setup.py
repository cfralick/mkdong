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


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

NAME = os.path.basename(BASE_DIR)

LICENSE='BSD-2-Clause'

AUTHOR='Jathan McCollum'

AUTHOR_EMAIL='jathan@gmail.com'

MAINTAINER='Clint Fralick'

MAINTAINER_EMAIL='cfralick@creeperengine.com'

URL='https://github.com/cfralick/mkdong'

PACKAGES = find_packages(exclude=['docs', 'tests*'])

EXTRAS_REQUIRE={
    'test': ['tox'],
    'dev': ['tox']
}

CUSTOM_COMMANDS={'test': Tox}

KEYWORDS=('penis', 'dong', 'cli',)

CLASSIFIERS=(
    'Environment :: Console',
    'Development Status :: 3 - Alpha',
    'Intended Audience :: All',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3'
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
    LONG_DESCRIPTION = descr.read().strip()


setup(
    name=NAME,
    version=VERSION,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=KEYWORDS,
    url=URL,
    packages=PACKAGES,
    tests_require=['tox','virtualenv'],
    extras_require=EXTRAS_REQUIRE,
    cmdclass=CUSTOM_COMMANDS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    entry_points=ENTRY_POINTS
)
