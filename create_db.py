import sqlite3

def create_db():
    # read sql-script filew
    with open('script.sql', 'r') as f:
        sql = f.read()

    # create connection with db
    with sqlite3.connect('student-progress.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ == '__main__':
    create_db()