class question(object):
    def __init__(self):
        import sqlite3
        db = sqlite3.connect(':memory:')
        cursor = db.cursor()
        db = addTable(db, cursor)
        db = insertToDatabase(db, cursor)
        db = insertToDatabase(db, cursor)
        retrieveData1(db, cursor)

        def addTable(db, cursor):
            # Get a cursor object
            # creates table QuestionBase
            cursor.execute(
                '''CREATE TABLE QuestionBase(id INTEGER PRIMARY KEY, notebookFile TEXT, created TEXT, modified TEXT, lastAttempt TEXT, difficulty TEXT, question TEXT)''')
            db.commit()
            return db

        def dropTable(db, cursor):
            cursor = db.cursor
            cursor.execute("""DROP TABLE QuestionBase""")
            db.commit()

            return db

        def insertToDatabase(db, cursor):
            # One row of data
            notebookFile = "notebookfile"
            created = "created"
            modified = "modified"
            lastAttempt = "lastattempt"
            difficulty = "difficulty"
            question = "question"

            # Inserts info into db
            cursor.execute(
                '''INSERT INTO QuestionBase(notebookFile, created, modified, lastAttempt, difficulty, question) VALUES(?,?,?,?,?,?)''',
                (notebookFile, created, modified, lastAttempt, difficulty, question))

            # print("inserted")

            db.commit()

            # prints out data (temporary)
            """
            with db:
                cursor.execute("SELECT * FROM QuestionBase")
                print(cursor.fetchall())
            """
            return db

        def retrieveData1(db, cursor):
            cursor.execute("""SELECT notebookFile, created FROM QuestionBase""")
            data = cursor.fetchone()
            print(data)

            return data

#object = question()

