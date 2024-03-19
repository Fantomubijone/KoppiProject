import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image
import customtkinter as ctk
from customtkinter import *
from database import DB  # Import the DB class


def clear():
    for widget in root.winfo_children():
        widget.destroy()

def center_window(root):
    # Calculate screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate window width and height
    window_width = 1024
    window_height = 768

    # Calculate position for centering the window
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set window geometry and position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Doesn't allow for resizing
    root.resizable(0, 0)

def logo(root):
    pic = CTkImage(dark_image=Image.open("StarbucksLogo.png"), 
                   light_image=Image.open("StarbucksLogo.png"), size=(400,400))
    logo = ctk.CTkLabel(root, text='', image=pic)
    logo.pack(pady=(70, 0))


# STARTING PAGE
def homepage(root):
    clear()
    logo(root)

    # Create a frame to hold the label texts
    text_frame = Frame(root)
    text_frame.pack()

    # Text before the bold part
    text_before_bold = "IT'S NOT JUST COFFEE, IT'S"
    label_before_bold = tk.Label(text_frame, text=text_before_bold, font=("Helvetica", 25))
    label_before_bold.pack(side=LEFT)

    # Bold part
    bold_part = "STARBUCKS"
    label_bold = tk.Label(text_frame, text=bold_part, font=("Helvetica", 25, "bold"), fg="#00754A")
    label_bold.pack(side=LEFT)

    get_started_button = ctk.CTkButton(root, text="Get Started",
                                       corner_radius=50, fg_color="#00754A",
                                       font=("Montserrat", 24), width=200, height=50,
                                       command=lambda: signup_page(root))
    get_started_button.pack(pady=(20, 0))



# SIGN UP
def signup_page(root):
    clear()
    # Create and display signup page
    signup_frame = Frame(root)
    signup_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    signup_label = tk.Label(signup_frame, text="Create an Account", font=("Segoe UI", 30, "bold"))  # Modern font and color
    signup_label.grid(row=0, column=0, columnspan=2, pady=30)

    # * indicates required field
    required_label = tk.Label(signup_frame, text="* Indicates required field", font=("Segoe UI", 10))  # Gray color for hint
    required_label.grid(row=1, column=0, padx=20, pady=(0,10))

    # Personal Information
    personal_info_label = tk.Label(signup_frame, text="Personal Information", font=("Segoe UI", 15, "bold"))  # Color adjustment
    personal_info_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=20, pady=(0,10))

    # First Name
    first_name_label = tk.Label(signup_frame, text="First Name:", font=("Segoe UI", 10))
    first_name_label.grid(row=3, column=0, sticky="w", padx=20)
    first_name_entry = ctk.CTkEntry(signup_frame, placeholder_text ="First Name")
    first_name_entry.grid(row=3, column=1, sticky="w", padx=(0, 20))

    # Last Name
    last_name_label = tk.Label(signup_frame, text="Last Name:", font=("Segoe UI", 10))
    last_name_label.grid(row=4, column=0, sticky="w", padx=20)
    last_name_entry = ctk.CTkEntry(signup_frame)  # Border adjustment
    last_name_entry.grid(row=4, column=1, sticky="w", padx=(0, 20))

    # Email
    email_label = tk.Label(signup_frame, text="Email:", font=("Segoe UI", 10))
    email_label.grid(row=5, column=0, sticky="w", padx=20)
    email_entry = ctk.CTkEntry(signup_frame)  # Border adjustment
    email_entry.grid(row=5, column=1, sticky="w", padx=(0, 20))

    # Mobile Number
    mobile_label = tk.Label(signup_frame, text="Mobile Number:", font=("Segoe UI", 10))
    mobile_label.grid(row=6, column=0, sticky="w", padx=20)
    mobile_entry = ctk.CTkEntry(signup_frame)  # Border adjustment
    mobile_entry.grid(row=6, column=1, sticky="w", padx=(0, 20))

    # Account Security
    account_security_label = tk.Label(signup_frame, text="Account Security", font=("Segoe UI", 15, "bold"))  # Color adjustment
    account_security_label.grid(row=7, column=0, columnspan=2, sticky="w", padx=20, pady=(20,10))

    # Username
    username_label = tk.Label(signup_frame, text="Username:", font=("Segoe UI", 10))
    username_label.grid(row=8, column=0, sticky="w", padx=20)
    username_entry = ctk.CTkEntry(signup_frame)  # Border adjustment
    username_entry.grid(row=8, column=1, sticky="w", padx=(0, 20))

    # Password
    password_label = tk.Label(signup_frame, text="Password:", font=("Segoe UI", 10))
    password_label.grid(row=9, column=0, sticky="w", padx=20)
    password_entry = ctk.CTkEntry(signup_frame, show="*")  # Border adjustment and password masking
    password_entry.grid(row=9, column=1, sticky="w", padx=(0, 20))

    # go to login
    goto_login = tk.Label(signup_frame, text="I already have an account", font=("Segoe UI", 10), fg="#00754A", cursor="hand2")
    goto_login.grid(row=10, column=0, columnspan=2, pady=(0,10))
    goto_login.bind("<Button-1>", lambda event: login_page(root))

    submit_button = ctk.CTkButton(signup_frame, text="Create Account",
                                  corner_radius=50, fg_color="#00754A",
                                  font=("Montserrat", 10), width=120, height=30,
                                  command=lambda: submit_signup_form(root, first_name_entry.get(),
                                                                     last_name_entry.get(), email_entry.get(),
                                                                     mobile_entry.get(), username_entry.get(),
                                                                     password_entry.get()))
    submit_button.grid(row=11, column=0, columnspan=2, pady=(10, 0))


# SIGN UP VALIDATION
def submit_signup_form(root, first_name, last_name, email, mobile_number, username, password):
    if not all([first_name, last_name, email, mobile_number, username, password]):
        messagebox.showerror("Error", "Please fill in all the fields.")
        return  
    
    db = DB("KoppiProject.db")  # Pass the database name when creating an instance of DB
    db.insert_into_accounts(first_name, last_name, email, mobile_number, username, password)

    # After inserting data into the database, you can perform any necessary actions
    messagebox.showinfo("Success", "Sign up successful!")
    homepage(root)  # Go back to the homepage


# LOGIN PAGE
def login_page(root):
    clear()
    # Create and display signup page
    login_frame = Frame(root)
    login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    login_label = tk.Label(login_frame, text="Sign in to your account", font=("Segoe UI", 30, "bold"))  # Modern font and color
    login_label.grid(row=0, column=0, columnspan=2, pady=30)

    # * indicates required field
    required_label = tk.Label(login_frame, text="* Indicates required field", font=("Segoe UI", 10))  # Gray color for hint
    required_label.grid(row=1, column=0, columnspan=2, pady=(0,10))

    # Username
    username_label = tk.Label(login_frame, text="Username:", font=("Segoe UI", 10))
    username_label.grid(row=2, column=0, sticky="w", padx=20)
    username_entry = ctk.CTkEntry(login_frame)  # Border adjustment
    username_entry.grid(row=2, column=1, sticky="w", padx=(0, 20))

    # Password
    password_label = tk.Label(login_frame, text="Password:", font=("Segoe UI", 10))
    password_label.grid(row=3, column=0, sticky="w", padx=20)
    password_entry = ctk.CTkEntry(login_frame, show="*")  # Border adjustment and password masking
    password_entry.grid(row=3, column=1, sticky="w", padx=(0, 20), pady=(0, 20))

    # go to login
    goto_signup = tk.Label(login_frame, text="I already have an account", font=("Segoe UI", 10), fg="#00754A", cursor="hand2")
    goto_signup.grid(row=4, column=0, columnspan=2, pady=(0,10))
    goto_signup.bind("<Button-1>", lambda event: signup_page(root))

    # Login Button
    login_button = ctk.CTkButton(login_frame, text="Sign In",
                                  corner_radius=50, fg_color="#00754A",
                                  font=("Montserrat", 19), width=150, height=40,
                                  command = lambda:login(username_entry.get(), password_entry.get()))
    login_button.grid(row=5, column=0, columnspan=2, pady=(20, 0))

# LOGIN VALIDATION
def login(username, password):
    # Validate the login
    db = DB("KoppiProject.db")
    if db.validate_login(username, password):
        messagebox.showinfo("Success", "Login Successful!")
        buy(root)
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def buy(root):
    pass

# MAIN 
if __name__ == "__main__":
    root = tk.Tk()
    set_appearance_mode("light")
    set_default_color_theme("green")
    root.title("Ordering System")
    center_window(root)

    homepage(root)

    root.mainloop()
