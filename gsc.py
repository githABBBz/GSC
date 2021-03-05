# MIT License

# Copyright (c) 2021 Joao Ferreira

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__all__ = ['LimitError', 'GoldSilverCopper', 'color']

from colorama import deinit, init

MAX = 9999999999999
MIN = 0


class LimitError(Exception):
    """"""


class GoldSilverCopper:
    def __init__(self):
        self.gsc = 0

    def add(self, g, s, c):
        g *= 10000
        s *= 100

        gsc = self.gsc + g + s + c

        if gsc > MAX:
            raise LimitError

        self.gsc = gsc

    def sub(self, g, s, c):
        g *= 10000
        s *= 100

        gsc = self.gsc - (g + s + c)

        if gsc < MIN:
            raise LimitError

        self.gsc = gsc

    def __repr__(self):
        gsc = str(self.gsc)

        g = gsc[:-4]
        s = gsc[-4:-2]
        c = gsc[-2:]

        if g:
            g = f'{g}g'

        if s:
            s = f'{s}s'
        c = f'{c}c'

        return f'{g}{s}{c}'


def color():
    msg_g = '\033[33mg\033[39m'
    msg_s = '\033[37ms\033[39m'
    msg_c = '\033[31mc\033[39m'

    init()

    try:
        while True:
            gsc = yield
            gsc = repr(gsc)
            gsc = gsc.replace('g', msg_g)
            gsc = gsc.replace('s', msg_s)
            gsc = gsc.replace('c', msg_c)
            print(gsc)
    finally:
        deinit()
