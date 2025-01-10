from PIL import Image
from customtkinter import *
import os
import sys

app = CTk()
app.title("Login")
app.geometry('600x600')

# Set the initial theme to light
appearance_mode = "light"
set_appearance_mode(appearance_mode)

# Function to toggle theme
def toggle_theme(theme_switch):
    global appearance_mode
    if appearance_mode == "light":
        set_appearance_mode("dark")
        theme_switch.configure(text="Dark Mode")
        appearance_mode = "dark"
    else:
        set_appearance_mode("light")
        theme_switch.configure(text="Light Mode")
        appearance_mode = "light"

# Function to handle login
attempts = 0

def login():
    global attempts
    entered_password = password_entry.get()
    if entered_password == "Password":
        password()  # Call your predefined function
    else:
        attempts += 1
        if attempts >= 6:
            result_lbl.configure(text="Be Silly!!")
        elif attempts >= 3:
            result_lbl.configure(text="Follow instructions!")
        else:
            result_lbl.configure(text="Invalid input.")
    password_entry.delete(0, END)

result_lbl = CTkLabel(app, text="", font=("Terminal", 14), text_color="red")
result_lbl.place(relx=0.5, rely=0.8, anchor="center")

# Theme toggle switch
theme_switch = CTkSwitch(
    master=app, 
    text="Light Mode",
    command=lambda: toggle_theme(theme_switch), 
    onvalue="dark", 
    offvalue="light"
)
theme_switch.place(relx=0.85, rely=0.1, anchor="center")

# Title CTkLabel
lbl = CTkLabel(
    master=app, 
    text="Enter Password", 
    font=("Terminal", 50)
)
lbl.place(relx=0.5, rely=0.3, anchor="center")

# Password entry
global password_entry
password_entry = CTkEntry(
    master=app,
    width=200,
    placeholder_text="Enter your password",
    show="•"  # Hides the text as asterisks
)
password_entry.place(relx=0.5, rely=0.5, anchor="center")

# Login button
login_button = CTkButton(
    master=app, 
    text="Login",
    font=("Terminal",20), 
    command=login
)
login_button.place(relx=0.5, rely=0.6, anchor="center")
def on_return_key(event):
    login_button.invoke()

app.bind('<Return>', on_return_key)

# Placeholder for the password function
def password():
    for widget in app.winfo_children():
        widget.destroy()
    
    # Password entry
    global password_entry
    password_entry = CTkEntry(
        master=app,
        width=200,
        placeholder_text="Enter your password",
        show="•"  # Hides the text as asterisks
    )
    password_entry.place(relx=0.5, rely=0.5, anchor="center")
    
    # Function to handle login
    def login():
        global attempts
        entered_password = password_entry.get()
        if entered_password == "Wrong":
            wrong()  # Call your predefined function
        else:
            attempts += 1
            if attempts >= 6:
                result_lbl.configure(text="Be Silly!!")
            elif attempts >= 3:
                result_lbl.configure(text="Follow instructions!")
            else:
                result_lbl.configure(text="Invalid input.")
        password_entry.delete(0, END)        
    
    result_lbl = CTkLabel(app, text="", font=("Terminal", 14),text_color="red")
    result_lbl.place(relx=0.5, rely=0.8, anchor="center")

    # Theme toggle switch
    theme_switch = CTkSwitch(
        master=app, 
        text="Light Mode", 
        command=lambda: toggle_theme(theme_switch), 
        onvalue="dark", 
        offvalue="light"
    )
    theme_switch.place(relx=0.85, rely=0.1, anchor="center")

    # Title CTkLabel
    lbl = CTkLabel(
        master=app, 
        text="Password is Wrong", 
        font=("Terminal", 50)
    )
    lbl.place(relx=0.5, rely=0.3, anchor="center")

    # Login button
    login_button = CTkButton(
        master=app, 
        text="Login", 
        font=("Terminal",20), 
        command=login
    )
    login_button.place(relx=0.5, rely=0.6, anchor="center")
    def on_return_key(event):
        login_button.invoke()

    app.bind('<Return>', on_return_key)

def wrong():
    for widget in app.winfo_children():
        widget.destroy()
    
    # Password entry
    global password_entry
    password_entry = CTkEntry(
        master=app,
        width=200,
        placeholder_text="Enter your password",
        show="•"  # Hides the text as asterisks
    )
    password_entry.place(relx=0.5, rely=0.5, anchor="center")
        
    # Function to handle login
    def login():
        global attempts
        entered_password = password_entry.get()
        if entered_password == "Again!":
            again()  # Call your predefined function
        else:
            attempts += 1
            if attempts >= 6:
                result_lbl.configure(text="Be Silly!!")
            elif attempts >= 3:
                result_lbl.configure(text="Follow instructions!")
            else:
                result_lbl.configure(text="Invalid input.")
        password_entry.delete(0, END)        

    result_lbl = CTkLabel(app, text="", font=("Terminal", 14),text_color="red")
    result_lbl.place(relx=0.5, rely=0.8, anchor="center")

    # Theme toggle switch
    theme_switch = CTkSwitch(
        master=app, 
        text="Light Mode", 
        command=lambda: toggle_theme(theme_switch), 
        onvalue="dark", 
        offvalue="light"
    )
    theme_switch.place(relx=0.85, rely=0.1, anchor="center")

    # Title CTkLabel
    lbl = CTkLabel(
        master=app, 
        text="Try Again!", 
        font=("Terminal", 50)
    )
    lbl.place(relx=0.5, rely=0.3, anchor="center")

    # Login button
    login_button = CTkButton(
        master=app, 
        text="Login", 
        font=("Terminal",20), 
        command=login
    )
    login_button.place(relx=0.5, rely=0.6, anchor="center")
    def on_return_key(event):
        login_button.invoke()

    app.bind('<Return>', on_return_key)


def again():
    for widget in app.winfo_children():
        widget.destroy()

    def resource_path(relative_path):
        try:
            # PyInstaller creates a temporary folder with `_MEIPASS`
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)    

    ending_image_path = resource_path('ending.png')
    endingimage = CTkImage(
        light_image=Image.open(ending_image_path),
        dark_image=Image.open(ending_image_path),
        size=(600, 600)
    )

    lbl = CTkLabel(
        master=app,
        text="",
        image=endingimage
    )
    lbl.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()

