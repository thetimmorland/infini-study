import sqlite3
from pathlib import Path

'''CREATE TABLE questions(id INTEGER PRIMARY KEY, notebook NONE,
created TEXT, modified TEXT, lastAttempt TEXT, difficulty TEXT,
question TEXT)'''

class db():
    def open(self, path):
        self.path = path
        self.conn = sqlite3.connect(path)

    def new(self, path):
        open(path, 'w+').close()
        self.open(path)

        cur = self.conn.cursor()

        cur.execute('''CREATE TABLE infinistudy
                (created TEXT, attempted TEXT, 
                question TEXT, notebook BLOB)'''
                )

        self.conn.commit()
        

class schedule():
    questions = []

    def __init__(self, db, numToStudy):
        cur = db.conn.cursor()

        cur.execute('SELECT * FROM infinistudy ORDER BY attempted ASC')
        self.questions = cur.fetchmany(numToStudy)

