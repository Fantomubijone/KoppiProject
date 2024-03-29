import sqlite3 # database
import random # for the receipt ref num
import os # for detecting existing txt file
from datetime import datetime # for the date today

class DB:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

        # Preloading tables
        self.create_accounts_table()
        self.create_menu_tables()  
        self.create_orders_table()
        self.create_current_user_table()
        
    # TABLE FOR ACCOUNTS    
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


    # TABLES FOR PRODUCTS
    def create_menu_tables(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS Drinks (
                            code_name TEXT PRIMARY KEY,
                            item_name TEXT,
                            tall_price REAL,
                            grande_price REAL,
                            venti_price REAL
                        )''')
        

        self.c.execute('''CREATE TABLE IF NOT EXISTS Pastries (
                            code_name TEXT PRIMARY KEY,
                            item_name TEXT,
                            price REAL
                        )''')
        

        self.c.execute('''CREATE TABLE IF NOT EXISTS Pasta (
                            code_name TEXT PRIMARY KEY,
                            item_name TEXT,
                            price REAL
                        )''')

        self.conn.commit()

        # DEFAULT DATA FOR MENU
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
                            username TEXT,
                            item_name TEXT,
                            price REAL,
                            quantity INTEGER
                        )''')
        self.conn.commit()

    def insert_into_orders(self, username, item_name, price, quantity):   
        self.c.execute('''INSERT INTO Orders (username, item_name, price, quantity)
                        VALUES (?, ?, ?, ?)''', (username, item_name, price, quantity))
        self.conn.commit()

    def fetch_orders_by_username(self, username):
        self.c.execute('''SELECT * FROM Orders WHERE username=?''', (username,))
        return self.c.fetchall()

    def delete_orders_by_username(self, username):
        self.c.execute('''DELETE FROM Orders WHERE username=?''', (username,))
        self.conn.commit()

    def delete_order(self, order_id):
        self.c.execute('''DELETE FROM Orders WHERE id=?''', (order_id,))
        self.conn.commit()

    def create_current_user_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS CurrentUser (
                            username TEXT PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            mobile_number TEXT,
                            password TEXT
                        )''')
        self.conn.commit()

    def set_current_user(self, username):
        # GETING USER DETAILS FROM ACCOUNT
        self.c.execute('''SELECT first_name, last_name, email, mobile_number, username, password FROM Accounts WHERE username=?''', (username,))
        user_details = self.c.fetchone()

        if user_details:
            self.c.execute('''INSERT OR REPLACE INTO CurrentUser (first_name, last_name, email, mobile_number, username, password)
                                VALUES (?, ?, ?, ?, ?, ?)''', user_details)  
            self.conn.commit()
        else:
            print("User not found in Accounts table.")


    def get_current_user_details(self):
        self.c.execute('''SELECT * FROM CurrentUser''')
        return self.c.fetchone()
    

    def get_current_username(self):
        self.c.execute('''SELECT username FROM CurrentUser''')
        username_row = self.c.fetchone()
        return username_row[0]
    

    def update_user_details(self, first_name, last_name, email, mobile_number, password, username):
        self.c.execute('''UPDATE CurrentUser SET first_name=?, last_name=?, email=?, mobile_number=?, password=? WHERE username=?''',
                        (first_name, last_name, email, mobile_number, password, username))
        self.conn.commit()

        self.c.execute('''UPDATE Accounts SET first_name=?, last_name=?, email=?, mobile_number=?, password=? WHERE username=?''',
                        (first_name, last_name, email, mobile_number, password, username))
        self.conn.commit()

    def get_codename(self, item_name):
        '''
        result[0] indicates the code_name from the respective products table
        '''

        # FOR DRINKS
        self.c.execute('''SELECT code_name FROM Drinks WHERE item_name=?''', (item_name,))
        result = self.c.fetchone()
        if result:
            return result[0] 
        
        # FOR PASTRIES
        self.c.execute('''SELECT code_name FROM Pastries WHERE item_name=?''', (item_name,))
        result = self.c.fetchone()
        if result:
            return result[0]

        # FOR PASTA
        self.c.execute('''SELECT code_name FROM Pasta WHERE item_name=?''', (item_name,))
        result = self.c.fetchone()
        if result:
            return result[0]
        return None  
    

    def initial_receipt(self):

        chk_number = random.randint(111111, 999999)
        current_time = datetime.now().strftime("%m/%d/%Y %I:%M %p")


        receipt = "\n              STARBUCKS Store  #112103\n"
        receipt += "           1892 11th Ave, Intramuros, Manila\n"
        receipt += "            VAT Reg Tin: 612-882-489-00000\n"
        receipt += "-" * 54 + "\n"
        receipt += f"                      CHK {chk_number}\n"
        receipt += f"                  {current_time}\n"
        receipt += "-" * 54 + "\n"
        receipt += "  {:<5}{:<20}  {:<10}  {:<10}\n".format("QTY", "CODENAME", "UNIT PRICE", "TOTAL PRICE")
        receipt += "-" * 54 + "\n"

        total_price = 0

        orders = self.fetch_orders_by_username(self.get_current_username())

        for order in orders:
            idorder, username, item_name, unit_price, quantity = order
            codename = self.get_codename(item_name)
            if codename:
                total_price += unit_price * quantity
                receipt += "  {:<5}{:<20}  {:<10.2f}  {:<10.2f}\n".format(quantity, codename, unit_price, unit_price * quantity)

        receipt += "\n\n       {:<34}{:<10.2f}\n".format("Subtotal", total_price)

        return receipt
    

    def receipt(self, payment, mode, change):
        receipt = self.initial_receipt()
        receipt += "       {:<34}{:<10.2f}\n".format(f"{mode}", payment)
        receipt += "       {:<34}{:<10.2f}\n".format("CHANGE DUE", change)
        receipt += self.footer()

        return receipt


    def footer(self):
        receipt = "\n-------------------- Check Closed --------------------\n\n"
        receipt += "         It's not just coffee. It's Starbucks.\n"
        receipt += "            For educational purposes only.\n"
        receipt += "                   www.starbucks.com\n"
        receipt += "          Folllow them on Twitter: @Starbucks\n"

        return receipt

    def calculate_total_due(self):
        total_price = 0

        orders = self.fetch_orders_by_username(self.get_current_username())

        for order in orders:
            idorder, username, item_name, unit_price, quantity = order
            codename = self.get_codename(item_name)
            if codename:
                total_price += unit_price * quantity

        return total_price
    

    def save_receipt_text(self, name, content):
        count = 0
        filename = f"{name}.txt"
        while os.path.exists(filename):
            count += 1
            filename = f"{name}({count}).txt"

        with open(filename, "w") as file:
            file.write(content)
            file.close()