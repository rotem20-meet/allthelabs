import tkinter as tk
from tkinter import simpledialog
year=2000

year == simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw())

if year <= 1900:
    print ('Woah, thats the past!')
elif year >= 1900 and year <= 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")

