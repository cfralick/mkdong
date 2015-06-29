# -*- coding: utf8 -*-

"""
mkdong main function
"""

from __future__ import absolute_import
import argparse
import sys
import os
from dong import Dong, DongTooLong


def terminal_width():
    """get the width of the current console."""
    import fcntl
    import termios
    import struct
    _, w, _, _ = struct.unpack('HHHH',
                               fcntl.ioctl(0, termios.TIOCGWINSZ,
                                           struct.pack('HHHH', 0, 0, 0, 0)))
    return w


def main():
    """Run mkdong."""

    base_path = os.path.dirname(os.path.dirname(__file__))

    version = open(os.path.join(base_path, 'VERSION')).read().strip()

    parser = argparse.ArgumentParser(
        description=Dong.__doc__,
        prog=os.path.basename(base_path),
        usage='%(prog)s <options> length [outfile]',
        epilog='%(prog)s ' + version)

    parser.add_argument(
        'length', type=int, default=0, nargs='?',
        help='the dong shaft length. Default: %(default)s')

    parser.add_argument(
        'outfile', type=argparse.FileType('w'),
        default=sys.stdout, nargs='?',
        help='save the dong to <outfile>. Optional')

    parser.add_argument(
        '-c', '--climax', action='count', default=0,
        help="make the dong climax. Can be used up to 5 times")

    parser.add_argument(
        '-w', '--wide', action='count', dest='width', default=0,
        help="make a wider, thicker dong. Can be used up to 3 times")

    parser.add_argument(
        '-v', '--version',
        action='version', version='%(prog)s ' + version)

    args = parser.parse_args()

    args.outfile.write(Dong(**vars(args)).__str__() + "\n")


if __name__ == '__main__':
    main()
