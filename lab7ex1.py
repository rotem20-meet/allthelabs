import tkinter as tk
from tkinter import simpledialog

#Then when ever you want to ask the user for input use this code:
greeting = simpledialog.askstring("Input" ,"Hello ossible pirate! Whats the password?", parent=tk.Tk().withdraw())
if greeting in ("Arrr!"):
	print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")

