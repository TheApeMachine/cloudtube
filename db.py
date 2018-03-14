import sqlite3

class DB:

    def __init__(self):
        self.connection = sqlite3.connect('filesystem')
        self.cursor     = self.connection.cursor()

        self.setup()

    def setup(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS files(id INTEGER PRIMARY KEY, name TEXT, fid TEXT unique)
        ''')

    def insert(self, name, fid):
        self.cursor.execute('''
            INSERT INTO files(name, fid) VALUES(?, ?)
        ''', name, fid)

        self.connection.commit()

    def file_list(self):
        self.cursor.execute('''
            SELECT * FROM files
        ''')

        return self.cursor.fetchall()
