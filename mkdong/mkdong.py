# -*- coding: utf-8 -*-

"""
mkdong.mkdong

This module implements functions that create and print a dong of 
a specific length.

"""

class DongTooLong(ValueError):
    """Dong is longer than console is wide."""
    pass


class Dong(object):
    """Prints a dong"""
    WAD = '~'
    BALLS = '( )/( )'
    HEAD = 'D'
    WIDTH=('-','=','/','[]',)

    @classmethod
    def mkdong(cls, args):
        """Creates a dong of ``length`` length."""
        
        from itertools import chain 
        
        def part(char, times):
            """Assembles penis part."""
            return [char for _ in xrange(0, times)]
        
        shaft = part(cls.WIDTH[args.width], args.length)
        head = part(cls.HEAD, 1)
        load = part(cls.WAD, args.climax)
        balls = part(cls.BALLS, 1)
        
        return "".join(chain(balls, shaft, head, load))
        
    @classmethod
    def print_dong(cls, dong, outfile):
        """Prints a dong to specified output."""
        
        def terminal_width():
            """get the width of the current console."""
            import fcntl, termios, struct
            _,w,_,_ = struct.unpack('HHHH',
                fcntl.ioctl(0, termios.TIOCGWINSZ,
                struct.pack('HHHH', 0, 0, 0, 0)))
            return w
    
        term_width = terminal_width()
        if term_width > len(dong):
            outfile.write(dong + "\n")
        else:
            raise DongTooLong(DongTooLong.__doc__)
