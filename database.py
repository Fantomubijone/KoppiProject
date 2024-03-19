import sqlite3

class DB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_accounts_table()  # Create Accounts table if it doesn't exist

    def create_accounts_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS Accounts (
                            id INTEGER PRIMARY KEY,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            mobile_number TEXT NOT NULL,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL
                        )''')
        self.conn.commit()

    def insert_into_accounts(self, first_name, last_name, email, mobile_number, username, password):
        self.c.execute('''INSERT INTO Accounts (first_name, last_name, email, mobile_number, username, password)
                            VALUES (?, ?, ?, ?, ?, ?)''', (first_name, last_name, email, mobile_number, username, password))
        self.conn.commit()

    def validate_login(self, username, password):
        self.c.execute('''SELECT * FROM Accounts WHERE username=? AND password=?''', (username, password))
        result = self.c.fetchone()  # Fetch the first matching row
        if result:
            return True  # Login successful if the user exists with the provided credentials
        else:
            return False  # Login failed if no matching user found with the provided credentials