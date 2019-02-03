import sqlite3
import os.path

class problemDb():
    def create(self, path):

        # Create blank file
        open(path, 'w+').close()

        self.conn = sqlite3.connect(path)
        cur = self.conn.cursor()

        cur.execute('''CREATE TABLE infinistudy
                (id INTEGER PRIMARY KEY, created TEXT,
                attempted TEXT, question TEXT, notebook BLOB)'''
                )

        self.conn.commit()

    def load(self, path):
        self.conn = sqlite3.connect(path)

    def getRow(self, idx):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM infinistudy WHERE id=?', idx)
        row = cur.fetchall()

        self.conn.commit()
        return row
    def replaceRow(self, idx, arr):
        cur = self.conn.cursor()
        cur.execute('REPLACE INTO infinistudy VALUES (?,?,?,?) WHERE id=?',
                arr, idx)
        self.conn.commit()

    def appendRow(self, arr):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO infinistudy VALUES (?,?,?,?)', arr)
        self.conn.commit()

