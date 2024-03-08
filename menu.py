import tkinter as tk
from tkinter import messagebox 

menu = tk.Tk()

def sayHi():
    print("Success")
    messagebox.showinfo("Greeting", "Hello po")

menu.title("Koppi Project")
menu.geometry('400x300+30+30')

button = tk.Button(menu, text="Click me", command=sayHi)
button.pack()

menu.mainloop()