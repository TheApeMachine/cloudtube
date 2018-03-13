import sys
from curses import wrapper
from ui import UI
from store import Store

def main(stdscr):
    MENU    = UI(stdscr)
    STORE   = False
    FILE    = sys.argv[2]
    STORAGE = Store(FILE)

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
