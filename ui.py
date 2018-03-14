import curses
from curses import panel

class UI:

    def __init__(self, stdscr):
        self.stdscr = stdscr

        self.stdscr.clear()

        self.begin_x   = 20
        self.begin_y   = 7
        self.current_y = 1
        self.height    = 5
        self.width     = 40
        self.win       = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)
        self.pad       = curses.newpad(100, 100)

        self.pad.addch(10, 10, ord('a') + (10 * 10 + 10 * 10) % 26)
        self.pad.refresh(0, 0, 5, 5, 20, 75)

    def debug(self, text):
        self.stdscr.addstr(self.current_y, 1, ''.join(text), curses.A_REVERSE)
        self.stdscr.refresh()

        self.current_y += 1
