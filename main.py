"""
Name: Ahmed Affaan
Title: main.py
Folder: ProjectAlpha
Date: 03/11/2022
Country: Republic of Maldives
Code version: -
Description:
Credits to:
Credits to link: 
Note: Uncomment codes to execute and comment them when not in use.
"""

# Importing libraries.
from tkinter import *
from tkinter import messagebox
import webbrowser

# This function displays about information box.
def menubar_about_box():
    messagebox.showinfo(title="Project Alpha", message="Version:\nCommit:\nDate: 2022-11-03\nPython: 03.10.17\nOS: Windows_NT x64 10.0.22621\nSandboxed: No")

# This function will display main window.
def overview_gui_window():
    login_window.destroy() # Closing old window.

    # Overview window configurations.
    global overview_window
    overview_window = Tk()
    overview_window.title("Project Alpha") # Window title.
    overview_window.geometry("800x608") # Window dimensions.
    overview_window.resizable(False, False) # Keeping constant window dimension size.
    overview_window.configure(bg="#191414")

    # Displays overview window labels.
    overview_window_label1 = Label(overview_window, text="Overview", font=("consolas bold", 20), bg="#191414", fg="#FFFFFF", width=24, height=2)
    overview_window_label1.pack()
    overview_window_label1.place(x=200, y=0) # Label placement.

    # Configurations to center overview window on initial run.
    overview_window.update() # Refreshes the window.
    overview_window_width = overview_window.winfo_width() # Retrieves the window width.
    overview_window_height = overview_window.winfo_height() # Retrieves the window height.
    screen_width = overview_window.winfo_screenwidth() # Retrieves the screen width.
    screen_height = overview_window.winfo_screenheight() # Retrieves the screen height.
    x = int((screen_width / 2) - (overview_window_width / 2)) # Calculates x-axis.
    y = int((screen_height / 2) - (overview_window_height / 2)) # Calculates y-axis.
    overview_window.geometry(f"{overview_window_width}x{overview_window_height}+{x}+{y}") # Sets the window size to any screen center.

# This function will display login window.
def login_gui_window():
    splash_screen.destroy() # Closing old window.
    
    # Login Window configurations.
    global login_window
    login_window = Tk()
    login_window.title("Project Alpha") # Window title.
    login_window.geometry("800x608") # Window dimensions.
    login_window.resizable(False, False) # Keeping constant window dimension size.
    login_window.configure(bg="#191414")

    # Displays login window labels.
    login_window_label1 = Label(login_window, text="Login", font=("consolas bold", 20), bg="#191414", fg="#FFFFFF", width=24, height=2)
    login_window_label1.pack()
    login_window_label1.place(x=210, y=100) # Label placement.
    login_window_label2 = Label(login_window, text="We're so excited to see you again!", font=("consolas", 11), bg="#191414", fg="#555555")
    login_window_label2.pack()
    login_window_label2.place(x=255, y=160) # Label placement.

    # Login window's username, password entry and login button.
    login_window_username_entry = Entry(login_window, font=("consolas", 11), bg="#555555", fg="#FFFFFF",  highlightthickness=0, highlightbackground="#555555", width=35) # Username entry
    #login_window_username_entry.insert(0, "Username")
    login_window_username_entry.pack()
    login_window_username_entry.place(x=249, y=200) # Entry placement.
    login_window_password_entry = Entry(login_window, font=("consolas", 11), show="*", bg="#555555", fg="#FFFFFF",  highlightthickness=0, highlightbackground="#555555", width=35) # Password entry
    #login_window_password_entry.insert(0, "Password")
    login_window_password_entry.pack()
    login_window_password_entry.place(x=249, y=245) # Entry placement.
    login_window_radio_button = Radiobutton(login_window, text="Remember Me", font=("consolas", 11), bg="#191414", fg="#555555") # Remember me radio button.
    login_window_radio_button.pack()
    login_window_radio_button.place(x=250, y=280) # Remember me radio button placement.
    login_window_button = Button(login_window, text="LOG IN", font=("consolas bold", 11), bg="#1DB954", fg="#FFFFFF", height=2, width=5, command=overview_gui_window) # Button for login window.
    login_window_button.place(x=330, y=325, width=130)  # Button placement.

    # Configurations to center login window on initial run.
    login_window.update() # Refreshes the window.
    login_window_width = login_window.winfo_width() # Retrieves the window width.
    login_window_height = login_window.winfo_height() # Retrieves the window height.
    screen_width = login_window.winfo_screenwidth() # Retrieves the screen width.
    screen_height = login_window.winfo_screenheight() # Retrieves the screen height.
    x = int((screen_width / 2) - (login_window_width / 2)) # Calculates x-axis.
    y = int((screen_height / 2) - (login_window_height / 2)) # Calculates y-axis.
    login_window.geometry(f"{login_window_width}x{login_window_height}+{x}+{y}") # Sets the window size to any screen center.

# Splash screen window configurations.
splash_screen = Tk()
splash_screen.title("Project Alpha") # Window title.
splash_screen.geometry("800x608") # Window dimensions.
splash_screen.resizable(False, False) # Keeping constant window dimension size.
splash_screen.configure(bg="#191414")

# Splash screen menu bar and options.
splash_screen_menubar = Menu(splash_screen)
splash_screen.config(menu=splash_screen_menubar)
splash_screen_menuFile = Menu(splash_screen_menubar, tearoff=0) # File menu.
splash_screen_menubar.add_cascade(label="File", menu=splash_screen_menuFile)
splash_screen_menuFile.add_command(label="Add New Login")
splash_screen_menuFile.add_command(label="Add New Item")
splash_screen_menuFile.add_separator()
splash_screen_menuFile.add_command(label="Sync Wallet")
splash_screen_menuFile.add_command(label="Export Wallet")
splash_screen_menuFile.add_separator()
splash_screen_menuFile.add_command(label="Sync Wallet")
splash_screen_menuFile.add_command(label="Lock Wallet")
splash_screen_menuFile.add_command(label="Log Out", command=quit)
splash_screen_menuFile.add_separator()
splash_screen_menuFile.add_command(label="Quit Project Alpha", command=quit)
splash_screen_menuEdit = Menu(splash_screen_menubar, tearoff=0) # Edit menu.
splash_screen_menubar.add_cascade(label="Edit", menu=splash_screen_menuEdit)
splash_screen_menuEdit.add_command(label="Undo")
splash_screen_menuEdit.add_command(label="Redo")
splash_screen_menuEdit.add_separator()
splash_screen_menuEdit.add_command(label="Cut")
splash_screen_menuEdit.add_command(label="Copy")
splash_screen_menuEdit.add_command(label="Paste")
splash_screen_menuEdit.add_separator()
splash_screen_menuEdit.add_command(label="Copy Username")
splash_screen_menuEdit.add_command(label="Copy Password")
splash_screen_menuEdit.add_command(label="Copy Verification Code (TOTP)")
splash_screen_menuView = Menu(splash_screen_menubar, tearoff=0) # View menu.
splash_screen_menubar.add_cascade(label="View", menu=splash_screen_menuView)
splash_screen_menuView.add_command(label="Zoom In")
splash_screen_menuView.add_command(label="Zoom Out")
splash_screen_menuView.add_command(label="Reset Zoom")
splash_screen_menuView.add_separator()
splash_screen_menuView.add_command(label="Toggle Full Screen")
splash_screen_menuView.add_separator()
splash_screen_menuView.add_command(label="Reload")
splash_screen_menuView.add_command(label="Toggle Developer Tools")
splash_screen_menuAccount = Menu(splash_screen_menubar, tearoff=0) # Account menu.
splash_screen_menubar.add_cascade(label="Account", menu=splash_screen_menuAccount)
splash_screen_menuAccount.add_command(label="Premium Membership")
splash_screen_menuAccount.add_command(label="Change Password")
splash_screen_menuAccount.add_command(label="Two-Step Login")
splash_screen_menuAccount.add_command(label="Secure Phrase")
splash_screen_menuAccount.add_separator()
splash_screen_menuAccount.add_command(label="Delete Account")
splash_screen_menuWindow = Menu(splash_screen_menubar, tearoff=0) # Window menu.
splash_screen_menubar.add_cascade(label="Window", menu=splash_screen_menuWindow)
splash_screen_menuWindow.add_command(label="Minimize")
splash_screen_menuWindow.add_command(label="Hide to Tray")
splash_screen_menuWindow.add_command(label="Maximize")
splash_screen_menuWindow.add_separator()
splash_screen_menuWindow.add_command(label="Close", command=quit)
splash_screen_menuHelp = Menu(splash_screen_menubar, tearoff=0) # Help menu.
splash_screen_menubar.add_cascade(label="Help", menu=splash_screen_menuHelp)
splash_screen_menuHelp.add_command(label="Get Help")
splash_screen_menuHelp.add_command(label="Contact Us")
splash_screen_menuHelp.add_command(label="File a Bug Report")
splash_screen_menuHelp.add_separator()
splash_screen_menuHelp.add_command(label="Follow Us")
splash_screen_menuHelp.add_separator()
splash_screen_menuHelp.add_command(label="Go to Website", command=lambda:webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
splash_screen_menuHelp.add_separator()
splash_screen_menuHelp.add_command(label="Get Mobile App")
splash_screen_menuHelp.add_command(label="Get Browser Extension")
splash_screen_menuHelp.add_separator()
splash_screen_menuHelp.add_command(label="Check for Updates...")
splash_screen_menuHelp.add_command(label="About Project Alpha", command=menubar_about_box)

# Splash screen labels.
splash_screen_label1 = Label(splash_screen, text="Project Alpha", font=("consolas bold", 20), bg="#191414", fg="#FFFFFF")
splash_screen_label1.pack()
splash_screen_label1.place(x=300, y=255) # Label placement.
splash_screen_label2 = Label(splash_screen, text="Welcome to the official Project Alpha app\nIt's fast and secure", font=("consolas", 11), bg="#191414", fg="#555555")
splash_screen_label2.pack()
splash_screen_label2.place(x=235, y=320) # Label placement.

# Configurations to center splash screen window on initial run.
splash_screen.update() # Refreshes the window.
splash_screen_width = splash_screen.winfo_width() # Retrieves the window width.
splash_screen_height = splash_screen.winfo_height() # Retrieves the window height.
screen_width = splash_screen.winfo_screenwidth() # Retrieves the screen width.
screen_height = splash_screen.winfo_screenheight() # Retrieves the screen height.
x = int((screen_width / 2) - (splash_screen_width / 2)) # Calculates x-axis.
y = int((screen_height / 2) - (splash_screen_height / 2)) # Calculates y-axis.
splash_screen.geometry(f"{splash_screen_width}x{splash_screen_height}+{x}+{y}") # Sets the window size to any screen center.
splash_screen_button1 = Button(splash_screen, text="START REQUESTING", font=("consolas bold", 11), bg="#1DB954", fg="#FFFFFF", width=5, height=2, command=login_gui_window) # Button for splash screen.
splash_screen_button1.place(x=335, y=410, width=145) # Button placement.

# Loops all windows.
mainloop()
