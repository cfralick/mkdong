#!/usr/bin/env python
import os
import sys
import argparse

"""
Prints a dong of a specific length.
"""

__author__ = 'Jathan McCollum, Mark Ellzey Thomas'
__maintainer__ = 'Jathan McCollum'
__email__ = 'jathan@gmail.com'
__copyright__ = '2009-2013, Jathan McCollum'
__version__ = '5.0'


# static immutable penis parts
BALLS = '( )/( )'
HEAD = 'D'
CLIMAX='~~~~'

ENV_VAR_NAME = 'MEGADONG'
DEFAULT_MAXLEN = 40


MAXLEN = os.environ.get(ENV_VAR_NAME) or DEFAULT_MAXLEN


def parse_args():
    parser = argparse.ArgumentParser(
        description='Prints a dong.',
        prog='mkdong',
        epilog='mkdong %s' % __version__
    )
    parser.add_argument('length', 
                        metavar='l', 
                        type=int, 
                        help='the desired dong length')
    
    parser.add_argument('-c', 
                        '--climax', 
                        action='store_true',
                        help='makes the dong climax')

    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version='%(prog)s ' + __version__,
                        help='print version and exit')
    
    dong_args = parser.parse_args()
    donglen = dong_args.length
    climax = dong_args.climax
    
    if donglen > MAXLEN:
        parser.error("error: a %s\" dong is too big! "
                         "cannot be longer than %s\"!" %
                         (donglen, MAXLEN))

    return (donglen, climax,)


def mkdong(length, climax=None):
    """Prints a dong of ``length`` length."""
    shaft = []
    for i in xrange(length):
        shaft.append('/')
    dong = [BALLS, ''.join(shaft), HEAD]
    
    if climax:
        dong.append(CLIMAX)

    return ''.join(dong)


def main():
    donglen,climax = parse_args()
    try:
        dong = mkdong(donglen, climax)
    except ValueError as ronjeremy:
        sys.exit(str(ronjeremy))
    else:
        os.system('echo "%s"' % dong)
