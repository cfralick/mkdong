# -*- coding: utf-8 -*-

"""
mkdong.dong

This module implements functions that create and print a dong of
a specific length.

"""


class Dong(object):
    """This class represents a dick."""
    COCKPRINT = '{nad}/{nad}{width:{width}<{length}}{head:~<{climax}}'

    DEFAULTS = {'length': 0, 'width': 0, 'nad': '( )', 'head': 'D'}

    WIDTHS = ('-', '=', '/',)

    def __init__(penis, **dongargs):
        penis.dongargs = penis.args(**dongargs)
        penis.__doc__ += penis.__repr__()

    def args(penis, **dongargs):
        dongargs.update(penis.convert_width(dongargs.get('width', 0)))
        kwds = Dong.DEFAULTS.copy()
        kwds.update(dongargs)
        return kwds

    def convert_width(penis, width):
        return dict(width=Dong.WIDTHS[width])

    def __repr__(penis):
        return Dong.COCKPRINT.format(**penis.dongargs)

    def __call__(penis):
        return penis.__repr__()

    def __str__(penis):
        return penis.__repr__()


class DongTooLong(ValueError):

    """Dong is longer than console is wide."""
    pass


def dong(**dongargs):
    return Dong(**dongargs)
