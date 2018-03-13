import curses
from curses import panel

class UI:

    def __init__(self, stdscr):
        self.stdscr = stdscr

        self.stdscr.clear()

        begin_x = 20
        begin_y = 7
        height  = 5
        width   = 40
        win     = curses.newwin(height, width, begin_y, begin_x)
        pad     = curses.newpad(100, 100)

        pad.addch(10, 10, ord('a') + (10 * 10 + 10 * 10) % 26)
        pad.refresh(0, 0, 5, 5, 20, 75)

        self.stdscr.addstr(0, 0, "Current Mode: STORAGE", curses.A_REVERSE)
        self.stdscr.refresh()
