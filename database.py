import sqlite3

class DB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_accounts_table()
        self.create_menu_tables()  
        self.create_orders_table()
        
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

    def create_menu_tables(self):
        # Create Drinks table
        self.c.execute('''CREATE TABLE IF NOT EXISTS Drinks (
                            code_name TEXT PRIMARY KEY,
                            item_name TEXT,
                            tall_price REAL,
                            grande_price REAL,
                            venti_price REAL
                        )''')
        
        # Create Pastries table
        self.c.execute('''CREATE TABLE IF NOT EXISTS Pastries (
                            code_name TEXT PRIMARY KEY,
                            item_name TEXT,
                            price REAL
                        )''')
        
        # Create Pasta table
        self.c.execute('''CREATE TABLE IF NOT EXISTS Pasta (
                            code_name TEXT PRIMARY KEY,
                            item_name TEXT,
                            price REAL
                        )''')

        self.conn.commit()

        # Insert menu data if not exists
        drinks_data = [
            ("FLT WHT", "Flat White", 170, 185, 200),
            ("CFF MST", "Caffe Misto", 115, 125, 135),
            ("ICD CPPCNO", "Iced Cappuccino", 145, 160, 175),
            ("ICD MRCN", "Iced Americano", 135, 150, 165),
            ("ICD CRML MCCHT", "Iced Caramel Macchiato", 170, 185, 200),
            ("MTCH GRN T", "Matcha Green Tea", 175, 190, 205),
            ("CHC CHP CRM", "Chocolate Chip Cream", 175, 190, 205),
            ("CRML", "Caramel", 160, 175, 190),
            ("MCH", "Mocha", 160, 175, 190),
            ("JV CH", "Java Chip", 175, 190, 205),
            ("ICD HBS T", "Iced Hibiscus Tea", 145, 160, 175),
            ("ICD SHKN T", "Iced Shaken Tea", 130, 145, 160),
            ("ICD CH T", "Iced Chai Tea", 160, 175, 190),
            ("ICD PR MCH", "Iced Pure Matcha", 160, 175, 190),
            ("ICD BLK T", "Iced Black Tea", 145, 160, 175),
            ("SGNTR HT CHC", "Signature Hot Chocolate", 155, 170, 185),
            ("WHT HT CHC", "White Hot Chocolate", 155, 170, 185)
        ]
        
        pastries_data = [
            ("CHC DPPD DGHNT", "Chocolate Dipped Doughnut", 87.5),
            ("TRPL CHS NSYMD", "Triple Cheese Ensaymada", 125),
            ("GLZD DGHNT", "Glazed Doughnut", 83),
            ("SSSG ND BCBN FLTBRT", "Sausage and Bacon Flatbread", 145),
            ("CNNMN DNSSH", "Cinnamon Danish", 132.14)
        ]
        
        pasta_data = [
            ("PNN PST WTH MSHRM", "Penne Pesto with Mushroom", 205),
            ("PLNT-BSD LSGN", "Plant-Based Classic Lasagna", 205)
        ]

        for item in drinks_data:
            self.c.execute('''INSERT OR IGNORE INTO Drinks (code_name, item_name, tall_price, grande_price, venti_price)
                                VALUES (?, ?, ?, ?, ?)''', item)

        for item in pastries_data:
            self.c.execute('''INSERT OR IGNORE INTO Pastries (code_name, item_name, price)
                                VALUES (?, ?, ?)''', item)

        for item in pasta_data:
            self.c.execute('''INSERT OR IGNORE INTO Pasta (code_name, item_name, price)
                                VALUES (?, ?, ?)''', item)

        self.conn.commit()

    def insert_into_accounts(self, first_name, last_name, email, mobile_number, username, password):
        self.c.execute('''INSERT INTO Accounts (first_name, last_name, email, mobile_number, username, password)
                            VALUES (?, ?, ?, ?, ?, ?)''', (first_name, last_name, email, mobile_number, username, password))
        self.conn.commit()


    def validate_login(self, username, password):
        self.c.execute('''SELECT * FROM Accounts WHERE username=? AND password=?''', (username, password))
        result = self.c.fetchone() 
        if result:
            return True
        else:
            return False
        
    def user_exists(self, username):
        self.c.execute('''SELECT * FROM Accounts WHERE username=?''', (username,))
        result = self.c.fetchone()
        if result:
            return True
        else:
            return False
        

    def create_orders_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS Orders (
                            id INTEGER PRIMARY KEY,
                            item_name TEXT,
                            price REAL,
                            quantity INTEGER
                        )''')
        self.conn.commit()

    def insert_into_orders(self, item_name, price, quantity):   
        self.c.execute('''INSERT INTO Orders (item_name, price, quantity)
                        VALUES (?, ?, ?)''', (item_name, price, quantity))
        self.conn.commit()

    def delete_orders(self): # To reset order
        self.c.execute('''DELETE FROM Orders''')
        self.conn.commit()

    def delete_order(self, order_id):
        self.c.execute('''DELETE FROM Orders WHERE id=?''', (order_id,))
        self.conn.commit()
