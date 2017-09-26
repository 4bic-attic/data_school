import sqlite3

class Database:
    """docstring for Database."""
    # constucts an object
    def __init__(self,db):
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book  VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        self.conn.close()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=cur.fetchall()
        conn.close()
        return rows

    def delete(self,id):
        cur.execute("DELETE FROM book  WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(self,id,title,author,year,isbn):
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        conn.commit()
        conn.close()

# connect to db everytime frontend is initiated