import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS users (
                         id INTEGER PRIMARY KEY,
                         first_name TEXT NOT NULL,
                         last_name TEXT NOT NULL,
                         username TEXT UNIQUE NOT NULL,
                         password TEXT NOT NULL,
                         email TEXT UNIQUE NOT NULL,
                         mobile TEXT NOT NULL
                         )''')
        self.conn.commit()

    def insert_user(self, first_name, last_name, username, password, email, mobile):
        try:
            self.c.execute("INSERT INTO users (first_name, last_name, username, password, email, mobile) VALUES (?, ?, ?, ?, ?, ?)",
                          (first_name, last_name, username, password, email, mobile))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def find_user(self, username, password):
        self.c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.c.fetchone()
        return user

    def close(self):
        self.conn.close()
