# -*- coding: utf8 -*-

"""
module mkdong.__main__

main function
"""

from __future__ import absolute_import
from dong import DongParser, mkdong


def main():
    """Run mkdong."""
    mkdong(DongParser().parse_args())

if __name__ == '__main__':
    main()
