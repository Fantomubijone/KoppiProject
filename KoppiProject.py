import tkinter as tk
from tkinter import messagebox
from database import Database

# Create database instance
db = Database('koppiproject.db')

class KoppiProjectApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Koppi Project")
        self.center_window()

        # Home Page
        self.home_frame = tk.Frame(self)
        self.home_frame.pack(pady=20)

        home_label = tk.Label(self.home_frame, text="IT’S NOT JUST COFFEE, IT’S KOPPI PROJECT", font=("Helvetica", 14))
        home_label.pack()

        get_started_button = tk.Button(self.home_frame, text="Get Started", command=self.show_login)
        get_started_button.pack()

        # Login Page
        self.login_frame = tk.Frame(self)

        login_label = tk.Label(self.login_frame, text="Login", font=("Helvetica", 14))
        login_label.grid(row=0, column=1, pady=10)

        username_label = tk.Label(self.login_frame, text="Username:")
        username_label.grid(row=1, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=1, column=1)

        password_label = tk.Label(self.login_frame, text="Password:")
        password_label.grid(row=2, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=2, column=1)

        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=1, pady=10)

        new_user_button = tk.Button(self.login_frame, text="New to Koppi Project? Sign Up", command=self.show_registration)
        new_user_button.grid(row=4, column=1)

        # Registration Page
        self.registration_frame = tk.Frame(self)

        registration_label = tk.Label(self.registration_frame, text="Registration", font=("Helvetica", 14))
        registration_label.grid(row=0, column=1, pady=10)

        first_name_label = tk.Label(self.registration_frame, text="First Name:")
        first_name_label.grid(row=1, column=0)
        self.first_name_entry = tk.Entry(self.registration_frame)
        self.first_name_entry.grid(row=1, column=1)

        last_name_label = tk.Label(self.registration_frame, text="Last Name:")
        last_name_label.grid(row=2, column=0)
        self.last_name_entry = tk.Entry(self.registration_frame)
        self.last_name_entry.grid(row=2, column=1)

        new_username_label = tk.Label(self.registration_frame, text="Username:")
        new_username_label.grid(row=3, column=0)
        self.new_username_entry = tk.Entry(self.registration_frame)
        self.new_username_entry.grid(row=3, column=1)

        new_password_label = tk.Label(self.registration_frame, text="Password:")
        new_password_label.grid(row=4, column=0)
        self.new_password_entry = tk.Entry(self.registration_frame, show="*")
        self.new_password_entry.grid(row=4, column=1)

        email_label = tk.Label(self.registration_frame, text="Email:")
        email_label.grid(row=5, column=0)
        self.email_entry = tk.Entry(self.registration_frame)
        self.email_entry.grid(row=5, column=1)

        mobile_label = tk.Label(self.registration_frame, text="Mobile:")
        mobile_label.grid(row=6, column=0)
        self.mobile_entry = tk.Entry(self.registration_frame)
        self.mobile_entry.grid(row=6, column=1)

        register_button = tk.Button(self.registration_frame, text="Register", command=self.register)
        register_button.grid(row=7, column=1, pady=10)

        self.show_home()

    def show_home(self):
        self.login_frame.pack_forget()
        self.registration_frame.pack_forget()
        self.home_frame.pack()

    def show_login(self):
        self.home_frame.pack_forget()
        self.registration_frame.pack_forget()
        self.login_frame.pack()

    def show_registration(self):
        self.home_frame.pack_forget()
        self.login_frame.pack_forget()
        self.registration_frame.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = db.find_user(username, password)

        if user:
            messagebox.showinfo("Login Successful", "Welcome back, " + user[1] + "!")
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def register(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        email = self.email_entry.get()
        mobile = self.mobile_entry.get()

        # Check if any fields are empty
        if not all([first_name, last_name, username, password, email, mobile]):
            messagebox.showerror("Registration Error", "Please fill in all fields.")
            return

        success = db.insert_user(first_name, last_name, username, password, email, mobile)
        
        if success:
            messagebox.showinfo("Registration Successful", "You have been registered successfully!")
            self.show_login()
        else:
            messagebox.showerror("Registration Error", "Username or email already exists.")

    def __del__(self):
        db.close()

    #center window 
    def center_window(self):
        # Calculate screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate window width and height
        window_width = 1024
        window_height = 768

        # Calculate position for centering the window
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Set window geometry and position
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Doesnt allow for resizing
        self.resizable(0,0)

app = KoppiProjectApp()
app.mainloop()
