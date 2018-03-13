import sys
from store import Store

def main():
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

if __name__ == "__main__":
    main()
