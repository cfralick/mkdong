#!/usr/bin/env python

"""
Prints a dong of a specific length.
"""
from __future__ import absolute_import
import itertools
import random
from collections import namedtuple

Defaults = namedtuple('Defaults', 'length choices head nad func cum width climax')

def repeat(token, times=1):
    return (token for _ in range(0, times))

def jizz(args):
    return repeat(args.cum, args.climax)

def balls(args):
    return (args.nad, '/', args.nad,)

def shaft(args):
    return repeat(args.width, args.length)

def head(args):
    return repeat(args.head)

def build_dong(args):
    return ''.join(itertools.chain(balls(args), shaft(args), head(args), jizz(args)))


Defaults = Defaults(
    head='D', 
    nad='( )', 
    length=random.randint(1,40), 
    choices=range(1,40),
    func=build_dong, 
    cum='~', 
    width='=', 
    climax=0
)
