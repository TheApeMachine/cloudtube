import sys
import curses
from curses import wrapper
from store import Store

def main(stdscr):
    STORE   = False
    FILE    = sys.argv[2]
    STORAGE = Store(FILE)

    stdscr.clear()

    begin_x = 20
    begin_y = 7
    height  = 5
    width   = 40
    win     = curses.newwin(height, width, begin_y, begin_x)
    pad     = curses.newpad(100, 100)

    pad.addch(10, 10, ord('a') + (10 * 10 + 10 * 10) % 26)
    pad.refresh(0, 0, 5, 5, 20, 75)

    stdscr.addstr(0, 0, "Current Mode: STORAGE", curses.A_REVERSE)
    stdscr.refresh()

    for arg in sys.argv:
        STORE = True

    if STORE:
        print('STORING ', FILE, '...')
        STORAGE.write()
    else:
        print('RETRIEVING ', FILE, '...')
        STORAGE(FILE, retrieve=True)

    print('ALL DONE!')

    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    wrapper(main)
