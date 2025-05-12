"""
Creating new window using tkinter: Unit Converter

'
import tkinter as tk

root = tk.Tk()



root.mainloop()
'

This will create a new window
"""

import tkinter as tk
from tkinter import font
from tkinter import messagebox
import pyqrcode
from PIL import Image, ImageTk

root = tk.Tk()
root.title("QR Generator")

img = None
def qr_function():
    generated_code = pyqrcode.create(entry.get())
    generated_code.png('qr_code.png', scale=8) # Image will save in current folder otherwise full path must be entered.
    # In case user forget to input:
    if entry.get().strip() == "":
        messagebox.showerror("Error", "Input text cannot be empty!") # This will show a warning if empty.
        return
    global img
    img = ImageTk.PhotoImage(Image.open('qr_code.png')) #cf
    qr.config(image=img)

def clear_qr():
    entry.delete(0, tk.END) # tk.END will clear all
    qr.config(image='')

header = tk.Label(root, text="QR Code Generator", font=font.Font(size=20), padx=8, pady=6)
header.grid(row=0, column=0, columnspan=2)

# Create entry box and take input
entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=2, padx=8, pady=6)

generator_button = tk.Button(root, text="Generate", command=qr_function)
generator_button.grid(row=2, column=0, sticky='ew')

clear_button = tk.Button(root, text="Clear", command=clear_qr)
clear_button.grid(row=2, column=1, sticky='ew')

qr = tk.Label(root, image='')
qr.grid(row=3, column=0, columnspan=2)


#finally
root.mainloop()