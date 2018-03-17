import sqlite3

database_path = "/Users/devashish/Desktop/Udemy/Python/bookkeeping-desktop-app/book_keeping.db"
class DB:
    def __init__(self):
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, author TEXT, year INTEGER, isbn TEXT)")
        conn.commit()
        conn.close()

    @staticmethod
    def insert(name, author, year, isbn):
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (name, author, year, isbn))
        conn.commit()
        conn.close()

    @staticmethod
    def view():
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        res = cur.fetchall()
        conn.close()
        return res

    @staticmethod
    def search(name="", author="", year="", isbn=""):
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE name=? OR author=? OR year=? OR isbn=?", (name, author, year, isbn))
        res = cur.fetchall()
        conn.close()
        return res

    @staticmethod
    def search_by_id(id):
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE id=?", (id,))
        res = cur.fetchall()
        conn.close()
        return res

    @staticmethod
    def update(_id, name, author, year, isbn):
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute("UPDATE books SET name=?, author=?, year=?, isbn=? WHERE id=?", (name, author, year, isbn, _id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id=?", (id,))
        conn.commit()
        conn.close()
