# -*- coding: utf8 -*-

"""
mkdong main function
"""

from __future__ import absolute_import
import argparse
import sys
import os
import mkdong
from mkdong import Dong, DongTooLong


def main():

    parser = argparse.ArgumentParser(
            description='Prints a dong.', prog=os.path.dirname(__file__),
            usage='%(prog)s <options> length', epilog='%(prog)s 6.1')

    parser.add_argument(
            'length', type=int, default=0, nargs='?',
            help='the dong shaft length. Default: %(default)s')

    parser.add_argument(
            'outfile', type=argparse.FileType('w'), 
            default=sys.stdout, nargs='?',
            help='save the dong to the specified file')

    parser.add_argument(
            '-c', '--climax', action='count', default=0, 
            help="make the dong climax. Can be used up to 5 times")

    parser.add_argument(
            '-w', '--wide', action='count', dest='width', default=0, 
            help="make a wider, thicker dong. Can be used up to 3 times")

    parser.add_argument(
            '-v', '--version', 
            action='version', version='%(prog)s 6.1')

    parser.set_defaults(dong=Dong.mkdong, put=Dong.print_dong)
    args = parser.parse_args()
    
    try:
        args.put(args.dong(args), args.outfile)
    except DongTooLong as toolong:
        sys.exit(str(toolong))

if __name__ == '__main__':
    main()
