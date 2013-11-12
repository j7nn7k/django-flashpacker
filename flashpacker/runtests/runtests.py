#!/usr/bin/env python

from __future__ import unicode_literals

import os
import sys


# adjusting sys.path
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..'))
sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'flashpacker.runtests.settings'


from django.conf import settings
from django.test.utils import get_runner


def usage():
    return """
    Usage: python runtests.py [UnitTestClass].[method]

    You can pass the Class name of the `UnitTestClass` you want to test.

    Append a method name if you only want to test a specific method of that class.
    """


def main():
    TestRunner = get_runner(settings)

    test_runner = TestRunner()

    failures = test_runner.run_tests(['flashpacker'])

    sys.exit(failures)


if __name__ == '__main__':
    main()
