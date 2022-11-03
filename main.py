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
