import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image
import customtkinter as ctk
from customtkinter import *
from database import DB 


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
                                       command=lambda: login_page(root))
    get_started_button.pack(pady=(20, 0))



# SIGN UP
def signup_page(root):
    clear()
    # Create and display signup page
    signup_frame = Frame(root)
    signup_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    signup_label = tk.Label(signup_frame, text="Create an Account", font=("Segoe UI", 30, "bold"))  
    signup_label.grid(row=0, column=0, columnspan=2, pady=30)

    # Personal Information
    personal_info_label = tk.Label(signup_frame, text="Personal Information", font=("Segoe UI", 15, "bold")) 
    personal_info_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=20, pady=(0,10))

    # First Name
    first_name_label = tk.Label(signup_frame, text="First Name:", font=("Segoe UI", 10))
    first_name_label.grid(row=2, column=0, sticky="w", padx=20)
    first_name_entry = ctk.CTkEntry(signup_frame)
    first_name_entry.grid(row=2, column=1, sticky="w", padx=(0, 20))

    # Last Name
    last_name_label = tk.Label(signup_frame, text="Last Name:", font=("Segoe UI", 10))
    last_name_label.grid(row=3, column=0, sticky="w", padx=20)
    last_name_entry = ctk.CTkEntry(signup_frame) 
    last_name_entry.grid(row=3, column=1, sticky="w", padx=(0, 20))

    # Email
    email_label = tk.Label(signup_frame, text="Email:", font=("Segoe UI", 10))
    email_label.grid(row=4, column=0, sticky="w", padx=20)
    email_entry = ctk.CTkEntry(signup_frame) 
    email_entry.grid(row=4, column=1, sticky="w", padx=(0, 20))

    # Mobile Number
    mobile_label = tk.Label(signup_frame, text="Mobile Number:", font=("Segoe UI", 10))
    mobile_label.grid(row=5, column=0, sticky="w", padx=20)
    mobile_entry = ctk.CTkEntry(signup_frame) 
    mobile_entry.grid(row=5, column=1, sticky="w", padx=(0, 20))

    # Account Security
    account_security_label = tk.Label(signup_frame, text="Account Security", font=("Segoe UI", 15, "bold")) 
    account_security_label.grid(row=6, column=0, columnspan=2, sticky="w", padx=20, pady=(20,10))

    # Username
    username_label = tk.Label(signup_frame, text="Username:", font=("Segoe UI", 10))
    username_label.grid(row=7, column=0, sticky="w", padx=20)
    username_entry = ctk.CTkEntry(signup_frame) 
    username_entry.grid(row=7, column=1, sticky="w", padx=(0, 20))

    # Password
    password_label = tk.Label(signup_frame, text="Password:", font=("Segoe UI", 10))
    password_label.grid(row=8, column=0, sticky="w", padx=20)
    password_entry = ctk.CTkEntry(signup_frame, show="*")  
    password_entry.grid(row=8, column=1, sticky="w", padx=(0, 20))

    # go to login
    goto_login = tk.Label(signup_frame, text="I already have an account", font=("Segoe UI", 10), fg="#00754A", cursor="hand2")
    goto_login.grid(row=9, column=0, columnspan=2, pady=20)
    goto_login.bind("<Button-1>", lambda event: login_page(root))

    submit_button = ctk.CTkButton(signup_frame, text="Create Account",
                                  corner_radius=50, fg_color="#00754A",
                                  font=("Montserrat", 13), width=120, height=30,
                                  command=lambda: submit_signup_form(root, first_name_entry.get(), last_name_entry.get(), email_entry.get(),mobile_entry.get(), username_entry.get(),password_entry.get()))
    
    submit_button.grid(row=10, column=0, columnspan=2)


# SIGN UP VALIDATION
def submit_signup_form(root, fname, lname, email, mobilenum, uname, passw):
    if not all([fname, lname, email, mobilenum, uname, passw]):
        messagebox.showerror("Error", "Please fill in all the fields.")
        return  
    
    db = DB("KoppiProject.db")  # Accesing the database file
    db.insert_into_accounts(fname, lname, email, mobilenum, uname, passw)

    messagebox.showinfo("Success", "Sign up successful!")
    login_page(root)


# LOGIN PAGE
def login_page(root):
    clear()
    # Create and display signup page
    login_frame = Frame(root)
    login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    login_label = tk.Label(login_frame, text="Sign in to Account", font=("Segoe UI", 30, "bold"))  
    login_label.grid(row=0, column=0, columnspan=2, pady=30)

    # Username
    username_label = tk.Label(login_frame, text="Username:", font=("Segoe UI", 10))
    username_label.grid(row=1, column=0, sticky="w", padx=20)
    username_entry = ctk.CTkEntry(login_frame) 
    username_entry.grid(row=1, column=1, sticky="w", padx=(0, 20))

    # Password
    password_label = tk.Label(login_frame, text="Password:", font=("Segoe UI", 10))
    password_label.grid(row=2, column=0, sticky="w", padx=20)
    password_entry = ctk.CTkEntry(login_frame, show="*")  
    password_entry.grid(row=2, column=1, sticky="w", padx=(0, 20))

    # go to login
    goto_signup = tk.Label(login_frame, text="Don't have any account?", font=("Segoe UI", 10), fg="#00754A", cursor="hand2")
    goto_signup.grid(row=3, column=0, columnspan=2, pady=20)
    goto_signup.bind("<Button-1>", lambda event: signup_page(root))

    # Login Button
    login_button = ctk.CTkButton(login_frame, text="Sign In",
                                  corner_radius=50, fg_color="#00754A",
                                  font=("Montserrat", 13), width=120, height=30,
                                  command = lambda:login(username_entry.get(), password_entry.get()))
    login_button.grid(row=4, column=0, columnspan=2)

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
    clear()
    category_frame = Frame(root)
    category_frame.pack(pady=20)

    def select_category(category):
        clear()
        print("Selected Category:", category)

    drinks_button = Button(category_frame, text="Drinks", font=("Helvetica", 16),
                           command=lambda: select_category("Drinks"))
    drinks_button.grid(row=0, column=0, padx=10)

    pastries_button = Button(category_frame, text="Pastries", font=("Helvetica", 16),
                             command=lambda: select_category("Pastries"))
    pastries_button.grid(row=0, column=1, padx=10)

    pasta_button = Button(category_frame, text="Pasta", font=("Helvetica", 16),
                          command=lambda: select_category("Pasta"))
    pasta_button.grid(row=0, column=2, padx=10)

    selected_category_label = Label(root, text="Please select a category", font=("Helvetica", 20))
    selected_category_label.pack(pady=50)

# MAIN 
if __name__ == "__main__":
    root = tk.Tk()
    set_appearance_mode("light")
    set_default_color_theme("green")
    root.title("Ordering System")
    center_window(root)

    homepage(root)

    root.mainloop()
