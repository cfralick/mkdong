#!/usr/bin/env python
import os
import sys
import argparse

"""
Makes dongs.
"""

__author__ = 'Jathan McCollum, Mark Ellzey Thomas'
__maintainer__ = 'Jathan McCollum'
__email__ = 'jathan@gmail.com'
__copyright__ = '2009-2013, Jathan McCollum'
__version__ = '5.0'

MAXLEN = os.environ.get('MEGADONG') or 40

# static immutable penis parts
BALLS = '( )/( )'
HEAD = 'D'
CLIMAX='~~~~'


def mkdong(length, climax=None):
    """Print a dong of ``length`` length."""
    shaft = []
    for i in xrange(length):
        shaft.append('/')
    dong = [BALLS, ''.join(shaft), HEAD]
    
    if climax:
        dong.append(CLIMAX)

    return ''.join(dong)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Make a dong.',
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
                        help='make a climaxing dong')

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


def main():
    donglen,climax = parse_args()
    try:
        dong = mkdong(donglen, climax)
    except ValueError as ronjeremy:
        sys.exit(str(ronjeremy))
    else:
        os.system('echo "%s"' % dong)
