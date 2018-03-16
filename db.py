import sqlite3


class DB:
    def __init__(self):
        conn = sqlite3.connect("book_keeping.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, price REAL, ISBN INTEGER)")
        conn.commit()
        conn.close()

    @staticmethod
    def insert(qry):
        conn = sqlite3.connect("book_keeping.db")
        cur = conn.cursor()
        cur.execute(qry)
        conn.commit()
        conn.close()

    @staticmethod
    def read(qry):
        conn = sqlite3.connect("book_keeping.db")
        cur = conn.cursor()
        cur.execute(qry)
        res = cur.fetchall()
        conn.close()
        return res

    @staticmethod
    def update(qry):
        conn = sqlite3.connect("book_keeping.db")
        cur = conn.cursor()
        cur.execute(qry)
        conn.commit()
        conn.close()

    @staticmethod
    def delete(qry):
        conn = sqlite3.connect("book_keeping.db")
        cur = conn.cursor()
        cur.execute(qry)
        conn.commit()
        conn.close()
