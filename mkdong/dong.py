
"""
mkdong.dong

This module implements functions that create and print a dong of
a specific length.

"""
import sys
import os
import argparse


class DongTooLong(ValueError):

    """Dong is too long to fit in terminal."""
    pass


class DongTooWide(ValueError):

    """No dong is this thick."""
    pass


class DongParser(argparse.ArgumentParser):

    """Prints a dong."""

    def __init__(self):
        super(
            DongParser,
            self).__init__(
            prog='mk' +
            __name__,
            description=self.__doc__,
            argument_default=0,
            epilog='0.1.1-dev0')
        self.add_argument(
            '-v',
            '--version',
            action='version',
            version='%(prog)s v{0!s}'.format('0.1.1-dev0'))
        self.add_argument(
            'length',
            nargs='?',
            type=int,
            help='the dong %(dest)s (default: %(default)s)')
        self.add_argument(
            '-c',
            '--climax',
            action='count',
            help="add a %(dest)s to %(prog)s's output")
        self.add_argument(
            '-o',
            '--outfile',
            nargs='?',
            type=argparse.FileType('w'),
            help="write %(prog)s's output to [%(dest)s]")
        self.add_argument(
            '-w',
            '--wide',
            dest='width',
            action='count',
            help="increase %(dest)s of %(prog)s's output")
        self.set_defaults(head='D', wad='~', outfile=sys.stdout)


class Dong(object):

    """This class represents a dick."""
    COCK_SPEC = '( )/( ){width:{width}<{length}}{head:{wad}<{climax}}'
    WIDTHS = ['-', '=', '/']
    dongargs = None

    def __init__(penis, **dongargs):
        dongargs['width'] = Dong.WIDTHS[dongargs.get('width', 0)]
        penis.__dict__.update(dongargs)

    def __format__(penis, format_spec=None):
        window = penis.terminal_width()
        if penis.length >= window and penis.outfile is sys.stdout:
            raise DongTooLong(DongTooLong.__doc__)
        
        return penis.COCK_SPEC.format(**penis.__dict__)

    def __str__(penis):
        return format(penis)

    def terminal_width(penis):
        """get the width of the current console."""
        import fcntl
        import termios
        import struct
        _, w, _, _ = struct.unpack(
            'HHHH', fcntl.ioctl(
                0, termios.TIOCGWINSZ, struct.pack(
                    'HHHH', 0, 0, 0, 0)))
        return w


def mkdong(dongargs):
    try:
        dong = str(Dong(**vars(dongargs)))
    except DongTooLong as megadong:
        dong = str(megadong)
    except IndexError as err:
        dong = str(err)
    except Exception as e:
        dong = str(e)
    finally:
        return dongargs.outfile.write(dong + "\n")
