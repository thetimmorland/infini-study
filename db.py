import sqlite3
from pathlib import Path


def newDb(self, path):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()

    cur.execute(
        '''CREATE TABLE questions(id INTEGER PRIMARY KEY, notebook NONE, created TEXT, modified TEXT, 
        lastAttempt TEXT, difficulty TEXT, question TEXT)''')

    cur.execute(
        '''INSERT INTO questions VALUES ('100', 'BRUH','2020', '2021', '2000', '8', 'WHY')'''
    )

    conn.commit()

    with path.open(mode='w') as output:
        for line in conn.iterdump():
            output.write(line + '\n')

    conn.close()

class scheduler():
    questions = []

    def __init__(self, path, num):
        conn = sqlite3.connect(path)
        cur = conn.cursor()

        allQuestions = cur.execute('SELECT * FROM questions ORDER BY lastAttempt ASC')
        print(allQuestions[:num])
