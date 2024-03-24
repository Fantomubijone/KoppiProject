import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image
import customtkinter as ctk
from customtkinter import *
from database import DB 

# TO REMOVE THE CONTENT AND PROCEED TO THE NEXT
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# FOR CENTERING WINDOW
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

# BUFFERING LOGO
def logo(root):
    pic = CTkImage(dark_image=Image.open("Images/Logo/StarbucksLogo.png"), 
                   light_image=Image.open("Images/Logo/StarbucksLogo.png"), size=(400,400))
    logo = ctk.CTkLabel(root, text='', image=pic)
    logo.pack(pady=(70, 0))

# CHECKOUT BUTTON
def checkout(root):
    checkout_button = Button(root, text="Checkout", command = lambda:homepage(root))
    checkout_button.place(relx=0.9, rely=0.9, anchor=SE)

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

    # * indicates required field
    required_label = tk.Label(signup_frame, text="* Indicates required field", font=("Segoe UI", 10))  
    required_label.grid(row=1, column=0, padx=20, pady=(0,10))

    # Personal Information
    personal_info_label = tk.Label(signup_frame, text="Personal Information", font=("Segoe UI", 15, "bold")) 
    personal_info_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=20, pady=(0,10))

    # First Name
    first_name_label = tk.Label(signup_frame, text="First Name:", font=("Segoe UI", 10))
    first_name_label.grid(row=3, column=0, sticky="w", padx=20)
    first_name_entry = ctk.CTkEntry(signup_frame)
    first_name_entry.grid(row=3, column=1, sticky="w", padx=(0, 20))

    # Last Name
    last_name_label = tk.Label(signup_frame, text="Last Name:", font=("Segoe UI", 10))
    last_name_label.grid(row=4, column=0, sticky="w", padx=20)
    last_name_entry = ctk.CTkEntry(signup_frame) 
    last_name_entry.grid(row=4, column=1, sticky="w", padx=(0, 20))

    # Email
    email_label = tk.Label(signup_frame, text="Email:", font=("Segoe UI", 10))
    email_label.grid(row=5, column=0, sticky="w", padx=20)
    email_entry = ctk.CTkEntry(signup_frame) 
    email_entry.grid(row=5, column=1, sticky="w", padx=(0, 20))

    # Mobile Number
    mobile_label = tk.Label(signup_frame, text="Mobile Number:", font=("Segoe UI", 10))
    mobile_label.grid(row=6, column=0, sticky="w", padx=20)
    mobile_entry = ctk.CTkEntry(signup_frame) 
    mobile_entry.grid(row=6, column=1, sticky="w", padx=(0, 20))

    # Account Security
    account_security_label = tk.Label(signup_frame, text="Account Security", font=("Segoe UI", 15, "bold")) 
    account_security_label.grid(row=7, column=0, columnspan=2, sticky="w", padx=20, pady=(20,10))

    # Username
    username_label = tk.Label(signup_frame, text="Username:", font=("Segoe UI", 10))
    username_label.grid(row=8, column=0, sticky="w", padx=20)
    username_entry = ctk.CTkEntry(signup_frame) 
    username_entry.grid(row=8, column=1, sticky="w", padx=(0, 20))

    # Password
    password_label = tk.Label(signup_frame, text="Password:", font=("Segoe UI", 10))
    password_label.grid(row=9, column=0, sticky="w", padx=20)
    password_entry = ctk.CTkEntry(signup_frame, show="*")  
    password_entry.grid(row=9, column=1, sticky="w", padx=(0, 20))

    # go to login
    goto_login = tk.Label(signup_frame, text="I already have an account", font=("Segoe UI", 10), fg="#00754A", cursor="hand2")
    goto_login.grid(row=10, column=0, columnspan=2, pady=20)
    goto_login.bind("<Button-1>", lambda event: login_page(root))

    submit_button = ctk.CTkButton(signup_frame, text="Create Account",
                                  corner_radius=50, fg_color="#00754A",
                                  font=("Montserrat", 13), width=120, height=30,
                                  command=lambda: submit_signup_form(root, first_name_entry.get(), last_name_entry.get(), email_entry.get(),mobile_entry.get(), username_entry.get(),password_entry.get()))
    
    submit_button.grid(row=11, column=0, columnspan=2)

# SIGN UP VALIDATION
def submit_signup_form(root, fname, lname, email, mobilenum, uname, passw):
    # Check if all fields are filled
    if not all([fname, lname, email, mobilenum, uname, passw]):
        messagebox.showerror("Error", "Please fill in all the fields.")
        return  

    # Check if mobile number is valid
    if len(mobilenum) != 11 or not mobilenum.isdigit():
        messagebox.showerror("Error", "Mobile number must be a 11-digit number.")
        return

    # Check if username already exists
    db = DB("KoppiProject.db")
    if db.user_exists(uname):
        messagebox.showerror("Error", "Username already exists. Please choose a different one.")
        return

    # If all validations pass, proceed with signup
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

    
    required_label = tk.Label(login_frame, text="* Indicates required field", font=("Segoe UI", 10))  
    required_label.grid(row=1, column=0, padx=20, pady=(0,10))

    # Username
    username_label = tk.Label(login_frame, text="Username:", font=("Segoe UI", 10))
    username_label.grid(row=2, column=0, sticky="w", padx=20)
    username_entry = ctk.CTkEntry(login_frame) 
    username_entry.grid(row=2, column=1, sticky="w", padx=(0, 20))

    # Password
    password_label = tk.Label(login_frame, text="Password:", font=("Segoe UI", 10))
    password_label.grid(row=3, column=0, sticky="w", padx=20)
    password_entry = ctk.CTkEntry(login_frame, show="*")  
    password_entry.grid(row=3, column=1, sticky="w", padx=(0, 20))

    # go to login
    goto_signup = tk.Label(login_frame, text="Don't have any account?", font=("Segoe UI", 10), fg="#00754A", cursor="hand2")
    goto_signup.grid(row=4, column=0, columnspan=2, pady=20)
    goto_signup.bind("<Button-1>", lambda event: signup_page(root))

    # Login Button
    login_button = ctk.CTkButton(login_frame, text="Sign In",
                                  corner_radius=50, fg_color="#00754A",
                                  font=("Montserrat", 13), width=120, height=30,
                                  command = lambda:login(username_entry.get(), password_entry.get()))
    login_button.grid(row=5, column=0, columnspan=2)

    # LOGIN VALIDATION
    def login(username, password):
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            return

        db = DB("KoppiProject.db")

        if db.user_exists(username):
            if db.validate_login(username, password):
                messagebox.showinfo("Success", "Login Successful!")
                buy(root)
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        else:
            messagebox.showerror("Error", "User not found!")
            create = messagebox.askquestion("Create an Account", "Would you like to make an account")
            if create == 'yes':
                signup_page(root)
            else:
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                password = ''
                username = ''

# SELECTING CATEGORY
def buy(root):
    clear()
    category_frame = Frame(root)
    category_frame.pack(pady=20)

    # Text label
    selected_category_label = Label(category_frame, text="Please select a category", font=("Helvetica", 30))
    selected_category_label.grid(row=0, column=0, columnspan=3, pady=(190, 30), sticky="n")

    dr_img = CTkImage(dark_image=Image.open("Images/Logo/Drinks.png"), 
                      light_image=Image.open("Images/Logo/Drinks.png"), size=(200, 200))
    imageDrinks = ctk.CTkLabel(category_frame, text='', image=dr_img)
    imageDrinks.grid(row=1, column=0, padx=10, pady=(0, 20), sticky="n")
    imageDrinks.bind("<Button-1>", lambda event: drink_catalog(root))

    drink_label = Label(category_frame, text='Drinks', font=("Helvetica", 20))
    drink_label.grid(row=2, column=0, padx=10, pady=(0, 20), sticky="n")

    pas_img = CTkImage(dark_image=Image.open("Images/Logo/Pasta.png"), 
                       light_image=Image.open("Images/Logo/Pasta.png"), size=(200, 200))
    imagePasta = ctk.CTkLabel(category_frame, text='', image=pas_img)
    imagePasta.grid(row=1, column=1, padx=10, pady=(0, 20), sticky="n")
    imagePasta.bind("<Button-1>", lambda event: pasta_subcategory(root))

    pasta_label = Label(category_frame, text='Pasta', font=("Helvetica", 20))
    pasta_label.grid(row=2, column=1, padx=10, pady=(0, 20), sticky="n")

    pst_img = CTkImage(dark_image=Image.open("Images/Logo/Pastries.png"), light_image=Image.open("Images/Logo/Pastries.png"), size=(200, 200))
    imagePastries = ctk.CTkLabel(category_frame, text='', image=pst_img)
    imagePastries.grid(row=1, column=2, padx=10, pady=(0, 20), sticky="n")  
    imagePastries.bind("<Button-1>", lambda event: pastries_subcategory(root))

    pastries_label = Label(category_frame, text='Pastries', font=("Helvetica", 20))
    pastries_label.grid(row=2, column=2, padx=10, pady=(0, 20), sticky="n")

    checkout(root)

# SELECTING WHAT KIND OF DRINK
def drink_catalog(root):
    clear()
    category_frame = Frame(root)
    category_frame.pack(pady=20)

    back_img = CTkImage(dark_image=Image.open("Images/Logo/Goback.png"), 
                        light_image=Image.open("Images/Logo/back.png"), size=(50, 50))
    back_button = ctk.CTkLabel(category_frame, text='', image=back_img)
    back_button.grid(row=0, column=0, padx=10, pady=(80, 40), sticky="nw")
    back_button.bind("<Button-1>", lambda event: buy(root)) 

    selected_kind = Label(category_frame, text="Select kind of drink", font=("Helvetica", 30))
    selected_kind.grid(row=1, column=0, columnspan=4, pady=(0, 50), sticky="n")

    # Espresso
    es_img = CTkImage(dark_image=Image.open("Images/Logo/Espresso.png"), 
                      light_image=Image.open("Images/Logo/Espresso.png"), size=(200, 200))
    imageEspresso = ctk.CTkLabel(category_frame, text='', image=es_img)
    imageEspresso.grid(row=2, column=0, padx=10, pady=(0, 20), sticky="n")
    imageEspresso.bind("<Button-1>", lambda event: drink_subcategory("Espresso"))

    espreso_label = Label(category_frame, text='Espresso', font=("Helvetica", 20))
    espreso_label.grid(row=3, column=0, padx=10, pady=(0, 20), sticky="n")

    # Frappuccino
    frap_img = CTkImage(dark_image=Image.open("Images/Logo/Frappuccino.png"), 
                        light_image=Image.open("Images/Logo/Frappuccino.png"), size=(200, 200))
    imageFrap = ctk.CTkLabel(category_frame, text='', image=frap_img)
    imageFrap.grid(row=2, column=1, padx=10, pady=(0, 20), sticky="n")
    imageFrap.bind("<Button-1>", lambda event: drink_subcategory("Frappuccino"))

    frap_label = Label(category_frame, text='Frappuccino', font=("Helvetica", 20))
    frap_label.grid(row=3, column=1, padx=10, pady=(0, 20), sticky="n")

    # Tea
    tea_img = CTkImage(dark_image=Image.open("Images/Logo/Tea.png"), light_image=Image.open("Images/Logo/Tea.png"), size=(200, 200))
    imageTea = ctk.CTkLabel(category_frame, text='', image=tea_img)
    imageTea.grid(row=2, column=2, padx=10, pady=(0, 20), sticky="n")  
    imageTea.bind("<Button-1>", lambda event: drink_subcategory("Tea"))

    Tea_label = Label(category_frame, text='Teavana Tea', font=("Helvetica", 20))
    Tea_label.grid(row=3, column=2, padx=10, pady=(0, 20), sticky="n")

    # Chocolate
    choco_img = CTkImage(dark_image=Image.open("Images/Logo/Chocolate.png"), light_image=Image.open("Images/Logo/Chocolate.png"), size=(200, 200))
    imageChoco = ctk.CTkLabel(category_frame, text='', image=choco_img)
    imageChoco.grid(row=2, column=3, padx=10, pady=(0, 20), sticky="n")  
    imageChoco.bind("<Button-1>", lambda event: drink_subcategory("Chocolate"))

    Choco_label = Label(category_frame, text='Chocolate', font=("Helvetica", 20))
    Choco_label.grid(row=3, column=3, padx=10, pady=(0, 20), sticky="n")

    checkout(root)
    
# DISPLAYING AND ORDERING SPECIFIC DRINK
def drink_subcategory(category):
    clear()
    left_frame = Frame(root)
    left_frame.place(relx=0.325, rely=0.5, anchor=CENTER)

    right_frame = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, padx=30,pady=30)
    right_frame.place(relx=0.775, rely=0.5, anchor=CENTER)

    back_img = CTkImage(dark_image=Image.open("Images/Logo/Goback.png"), 
                            light_image=Image.open("Images/Logo/back.png"), size=(30, 30))
    back_button = ctk.CTkLabel(left_frame, text='', image=back_img)
    back_button.grid(row=0, column=0, pady=(10, 20), sticky="nw")
    back_button.bind("<Button-1>", lambda event: drink_catalog(root)) 
    
    db = DB("KoppiProject.db")
    db.c.execute('''SELECT * FROM Drinks''')
    drinks_data = db.c.fetchall()

    if category == "Espresso":
        category_data = drinks_data[:5]
    elif category == "Frappuccino":
        category_data = drinks_data[5:10]
    elif category == "Tea":
        category_data = drinks_data[10:15]
    elif category == "Chocolate":
        category_data = drinks_data[15:]
    else:
        return

    # Displaying drink details and select button
    def select_item(item_name, tall_price, grande_price, venti_price):
        placeimg = CTkImage(dark_image=Image.open(f"Images/Drinks/{category}/{item_name}.png"),
                            light_image=Image.open(f"Images/Drinks/{category}/{item_name}.png"), size=(100, 100))
        selected_item_image_label.configure(image=placeimg)
        selected_item_name_label.config(text=item_name)

        tall_price_radio.config(text=f"Tall", value=tall_price, state="normal")
        grande_price_radio.config(text=f"Grande", value=grande_price, state="normal")
        venti_price_radio.config(text=f"Venti", value=venti_price, state="normal")

        quantity_entry.configure(state="normal")
        quantity_entry.delete(0,END)

        add_order_button.config(state="normal")
        tall_price_radio.invoke()

    def disable_onload():
        tall_price_radio.config(state="disabled")
        grande_price_radio.config(state="disabled")
        venti_price_radio.config(state="disabled")
        quantity_entry.configure(state="disabled")
        add_order_button.config(state="disabled")

    for i, drink in enumerate(category_data):
        code_name, item_name, tall_price, grande_price, venti_price = drink

        drink_img = CTkImage(dark_image=Image.open(f"Images/Drinks/{category}/{item_name}.png"),
                            light_image=Image.open(f"Images/Drinks/{category}/{item_name}.png"), size=(100, 100))

        drink_image_label = ctk.CTkLabel(left_frame, text='', image=drink_img)
        drink_image_label.grid(row=i+1, column=0, padx=10, pady=10)

        drink_label = Label(left_frame, text=item_name, font=("Helvetica", 16))
        drink_label.grid(row=i+1, column=1, padx=10, pady=10, sticky="w")

        prices_text = f"PRICE:\nTall: {tall_price:.0f}\nGrande: {grande_price:.0f}\nVenti: {venti_price:.0f}"
        prices_label = Label(left_frame, text=prices_text, justify="left")
        prices_label.grid(row=i+1, column=2, padx=10, pady=10)

        select_button = Button(left_frame, text="Select", 
                               command=lambda item=item_name, tall=tall_price, grande=grande_price, venti=venti_price:
                               select_item(item, tall, grande, venti))
        select_button.grid(row=i+1, column=3, padx=10, pady=10)

    # Order form
    order_label = Label(right_frame, text="Order Form", font=("Helvetica", 25, 'bold'))
    order_label.grid(row=0, column=0, columnspan=3)

    placeimg = CTkImage(dark_image=Image.open(f"Images/Logo/Product placeholder.png"),
                            light_image=Image.open(f"Images/Logo/Product placeholder.png"), size=(100, 100))
    
    selected_item_image_label = ctk.CTkLabel(right_frame, text='', image=placeimg)
    selected_item_image_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    selected_item_name_label = Label(right_frame, text="Select a Drink", font=("Helvetica", 18, 'bold'))
    selected_item_name_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    size_label = Label(right_frame, text="Size Option")
    size_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    drink_size_var = IntVar(right_frame)
    tall_price_radio = Radiobutton(right_frame, text="Tall", variable=drink_size_var, value=0)
    grande_price_radio = Radiobutton(right_frame, text="Grande", variable=drink_size_var, value=0)
    venti_price_radio = Radiobutton(right_frame, text="Venti", variable=drink_size_var, value=0)

    tall_price_radio.grid(row=4, column=0, padx=5, pady=10)
    grande_price_radio.grid(row=4, column=1, padx=5, pady=10)
    venti_price_radio.grid(row=4, column=2, padx=5, pady=10)

    quantity_entry = ctk.CTkEntry(right_frame, placeholder_text="Quantity", width=100, justify = 'center')
    quantity_entry.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    add_order_button = Button(right_frame, text="Add Order", 
                            command=lambda: add_order_to_db(selected_item_name_label["text"], drink_size_var.get(), quantity_entry.get(), quantity_entry))
    add_order_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
    checkout(root)
    disable_onload()

    def add_order_to_db(item_name, size, quantity, quantity_entry):
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a valid number.")
            quantity_entry.delete(0, END)
            return
            
        db.insert_into_orders(item_name, size, quantity)
        print(item_name)
        print(size)
        print(quantity)
        messagebox.showinfo("Order Added",f"{item_name} has been added.")
        quantity_entry.delete(0, END)

# DISPLAYING AND ORDERING SPECIFIC PASTA
def pasta_subcategory(root):
    clear()
    left_frame = Frame(root)
    left_frame.place(relx=0.325, rely=0.5, anchor=CENTER)  # Centering left frame

    right_frame = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, padx=30, pady=30)
    right_frame.place(relx=0.775, rely=0.5, anchor=CENTER)  # Centering right frame

    back_img = CTkImage(dark_image=Image.open("Images/Logo/Goback.png"), light_image=Image.open("Images/Logo/back.png"), size=(30, 30))
    back_button = ctk.CTkLabel(left_frame, text='', image=back_img)
    back_button.grid(row=0, column=0, pady=(10, 20), sticky="nw")
    back_button.bind("<Button-1>", lambda event: buy(root))

    db = DB("KoppiProject.db")
    db.c.execute('''SELECT * FROM Pasta''')
    pasta_data = db.c.fetchall()

    def select_pasta(item_name, price,):
        selected_item_name_label.config(text=item_name)
        price_label.config(text=f"Price: {price:.0f}")
        placeimg = CTkImage(dark_image=Image.open(f"Images/Pasta/{item_name}.png"),
                            light_image=Image.open(f"Images/Pasta/{item_name}.png"), size=(200, 200))
    
        selected_item_image_label.configure(image=placeimg)
        quantity_entry.configure(state="normal")
        quantity_entry.delete(0,END)
        add_order_button.configure(state='normal')


    def add_order_to_db(item_name, price, quantity, quantity_entry):
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a valid number.")
            quantity_entry.delete(0, END)
            return

        db.insert_into_orders(item_name, price, quantity)  # For pasta, size is not applicable
        messagebox.showinfo("Order Added", f"{item_name} has been added.")
        quantity_entry.delete(0, END)

    def disable_onload():
        quantity_entry.configure(state="disabled")
        add_order_button.config(state="disabled")

    for i, pasta_item in enumerate(pasta_data):
        code_name, item_name, price = pasta_item

        pasta_img = CTkImage(dark_image=Image.open(f"Images/Pasta/{item_name}.png"), 
                             light_image=Image.open(f"Images/Pasta/{item_name}.png"), size=(160, 160))

        pasta_image_label = ctk.CTkLabel(left_frame, text='', image=pasta_img)
        pasta_image_label.grid(row=i+1, column=0)

        pasta_label = Label(left_frame, text=item_name, font=("Helvetica", 16))
        pasta_label.grid(row=i+1, column=1, padx=10, pady=10, sticky="w")

        price_label = Label(left_frame, text=f"PRICE: {price:.0f}", justify="left")
        price_label.grid(row=i+1, column=2, padx=10, pady=10)

        select_button = Button(left_frame, text="Select", command=lambda item=item_name, price=price: select_pasta(item, price))
        select_button.grid(row=i+1, column=3, padx=10, pady=10)

    # Order form
    order_label = Label(right_frame, text="Order Form", font=("Helvetica", 25, 'bold'))
    order_label.grid(row=0, column=0, columnspan=3)


    placeimg = CTkImage(dark_image=Image.open(f"Images/Logo/Product placeholder.png"),
                            light_image=Image.open(f"Images/Logo/Product placeholder.png"), size=(100, 100))
    
    selected_item_image_label = ctk.CTkLabel(right_frame, text='', image=placeimg)
    selected_item_image_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    selected_item_name_label = Label(right_frame, text="Select a Pasta", font=("Helvetica", 18, 'bold'))
    selected_item_name_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    price_label = Label(right_frame, text="Price: $0.00")
    price_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    quantity_entry = ctk.CTkEntry(right_frame, placeholder_text="Quantity", width=100, justify='center')
    quantity_entry.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    add_order_button = Button(right_frame, text="Add Order", command=lambda: add_order_to_db(selected_item_name_label["text"], price, quantity_entry.get(), quantity_entry))
    add_order_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    checkout(root)
    disable_onload()

# DISPLAYING AND ORDERING SPECIFIC PASTRIES
def pastries_subcategory(root):
    clear()
    left_frame = Frame(root)
    left_frame.place(relx=0.325, rely=0.5, anchor=CENTER) 

    right_frame = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, padx=30, pady=30)
    right_frame.place(relx=0.775, rely=0.5, anchor=CENTER) 

    back_img = CTkImage(dark_image=Image.open("Images/Logo/Goback.png"), light_image=Image.open("Images/Logo/back.png"), size=(30, 30))
    back_button = ctk.CTkLabel(left_frame, text='', image=back_img)
    back_button.grid(row=0, column=0, pady=(10, 20), sticky="nw")
    back_button.bind("<Button-1>", lambda event: buy(root))

    db = DB("KoppiProject.db")
    db.c.execute('''SELECT * FROM Pastries''')
    pastries_data = db.c.fetchall()

    def select_pastries(item_name, price):
        selected_item_name_label.config(text=item_name)
        price_label.config(text=f"Price: {price:.2f}")  
        placeimg = CTkImage(dark_image=Image.open(f"Images/Pastries/{item_name}.png"),
                            light_image=Image.open(f"Images/Pastries/{item_name}.png"), size=(150, 150))

        selected_item_image_label.configure(image=placeimg)
        quantity_entry.configure(state="normal")
        quantity_entry.delete(0, END)
        add_order_button.configure(state='normal')


    def add_order_to_db(item_name, price, quantity, quantity_entry):
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a valid number.")
            quantity_entry.delete(0, END)
            return

        db.insert_into_orders(item_name, price, quantity)
        messagebox.showinfo("Order Added", f"{item_name} has been added.")
        quantity_entry.delete(0, END)

    def disable_onload():
        quantity_entry.configure(state="disabled")
        add_order_button.config(state="disabled")

    for i, pastries_item in enumerate(pastries_data):
        code_name, item_name, price = pastries_item

        pastri_img = CTkImage(dark_image=Image.open(f"Images/Pastries/{item_name}.png"), 
                             light_image=Image.open(f"Images/Pastries/{item_name}.png"), size=(120,120))

        pastri_image_label = ctk.CTkLabel(left_frame, text='', image=pastri_img)
        pastri_image_label.grid(row=i+1, column=0)

        pastri_label = Label(left_frame, text=item_name, font=("Helvetica", 16))
        pastri_label.grid(row=i+1, column=1, padx=10, pady=10, sticky="w")

        price_label = Label(left_frame, text=f"PRICE: {price:.2f}", justify="left")
        price_label.grid(row=i+1, column=2, padx=10, pady=10)

        select_button = Button(left_frame, text="Select", command=lambda item=item_name, price=price: select_pastries(item, price))
        select_button.grid(row=i+1, column=3, padx=10, pady=10)

    # Order form
    order_label = Label(right_frame, text="Order Form", font=("Helvetica", 25, 'bold'))
    order_label.grid(row=0, column=0, columnspan=3)


    placeimg = CTkImage(dark_image=Image.open(f"Images/Logo/Product placeholder.png"),
                            light_image=Image.open(f"Images/Logo/Product placeholder.png"), size=(100, 100))
    
    selected_item_image_label = ctk.CTkLabel(right_frame, text='', image=placeimg)
    selected_item_image_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    selected_item_name_label = Label(right_frame, text="Select a Pastry", font=("Helvetica", 18, 'bold'))
    selected_item_name_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    price_label = Label(right_frame, text="Price: 0.00")
    price_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    quantity_entry = ctk.CTkEntry(right_frame, placeholder_text="Quantity", width=100, justify='center')
    quantity_entry.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    add_order_button = Button(right_frame, text="Add Order", command=lambda: add_order_to_db(selected_item_name_label["text"], float(price_label['text'].replace("Price: ", "")), quantity_entry.get(), quantity_entry))
    add_order_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    checkout(root)
    disable_onload()

# MAIN 
if __name__ == "__main__":
    db = DB("KoppiProject.db")
    root = tk.Tk()
    set_appearance_mode("system")
    set_default_color_theme("green")
    root.title("Ordering System")
    center_window(root)

    try:
        # db.delete_orders()
        # homepage(root)
        buy(root)
    finally:
        # db.delete_orders()
        pass

    root.mainloop()