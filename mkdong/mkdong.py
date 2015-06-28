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
    """Static immutable penis parts"""
    WAD = '~'
    BALLS = '( )/( )'
    HEAD = 'D'
    WIDTH=('-','=','/','[]',)

    def __init__(self, args):
        self.length = args.length
        self.width = args.width
        self.climax = args.climax
        self.outfile = args.outfile

    def mkpart(self, part, times):
        return [part for _ in xrange(0, times)]

    def mkdong(self):
        """Creates a dong of ``length`` length."""
        
        from itertools import chain 
        
        shaft = self.mkpart(self.WIDTH[self.width], self.length)
        head = self.mkpart(self.HEAD, 1)
        load = self.mkpart(self.WAD, self.climax)
        balls = self.mkpart(self.BALLS, 1)
        
        dong = "".join(chain(balls, shaft, head, load))
       
        self.print_dong(dong)

    @staticmethod
    def terminal_width():
        """get the width of the current console."""
        import fcntl, termios, struct
        _,w,_,_ = struct.unpack('HHHH',
            fcntl.ioctl(0, termios.TIOCGWINSZ,
            struct.pack('HHHH', 0, 0, 0, 0)))
        return w
    

    def print_dong(self, dong):
        """Prints a dong to specified output."""
        
        term_width = Dong.terminal_width()
        if term_width > len(dong):
            self.outfile.write(dong + "\n")
        else:
            raise DongTooLong(DongTooLong.__doc__)
