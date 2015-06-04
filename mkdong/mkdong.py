#!/usr/bin/env python

"""
Prints dongs.
"""
from __future__ import absolute_import
import argparse
import sys
from mkdong.dong import Defaults

def parser(defaults):
    parser = argparse.ArgumentParser(
        description=__doc__,
    )

    parser.set_defaults(**defaults._asdict())

    parser.add_argument('length', 
                    type=int, 
                    choices=defaults.choices,
                    default=defaults.length,
                    nargs='?',
                    help='the desired dong shaft length')

    parser.add_argument('-t',
                    '--thin', 
                    action='store_const', 
                    const='-',
                    dest='width',
                    help='print a dong with a thin shaft')


    parser.add_argument('-w',
                    '--wide', 
                    action='store_const', 
                    const='/',
                    dest='width',
                    help='print a dong with a thick shaft')


    parser.add_argument('-c', 
                    '--climax', 
                    action='count',
                    help='Make the dong climax. May be used multiple times.')

    parser.add_argument('-v',
                    '--version',
                    action='version',
                    version='%(prog)s 0.0.1',
                    help='print version and exit')

    return parser

def main():
    args = parser(Defaults).parse_args()
    sys.exit(args.func(args))
