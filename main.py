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
splash_screen_button1 = Button(splash_screen, text="START REQUESTING", font=("consolas bold", 11), bg="#1DB954", fg="#FFFFFF", width=5, height=2) # Button for splash screen.
splash_screen_button1.place(x=335, y=410, width=145) # Button placement.

# Loops all windows.
mainloop()
