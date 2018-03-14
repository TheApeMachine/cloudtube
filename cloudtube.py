import sys
from curses import wrapper
from ui import UI
from db import DB
from store import Store

def main(stdscr):
    MENU    = UI(stdscr)
    STORE   = False
    FILE    = sys.argv[2]
    STORAGE = Store(FILE)
    DBASE   = DB()

    for arg in sys.argv:
        STORE = True

    if STORE:
        MENU.debug(['STORING ', FILE, '...'])
        STORAGE.write()
    else:
        MENU.debug(['RETRIEVING ', FILE, '...'])
        STORAGE(FILE, retrieve=True)

    MENU.debug(['ALL DONE!'])

    # Restore terminal to a sane state.
    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    wrapper(main)
