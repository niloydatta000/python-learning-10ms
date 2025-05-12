"""
Creating new window using tkinter: Basic

'
import tkinter as tk

root = tk.Tk()




root.mainloop()
'

This will create a new window
"""

import tkinter as tk

root = tk.Tk()
root.title("Converter") # Window title

# Take entry in box
labelText = tk.Label(root, text="Enter your number", padx=10, pady=10)
labelText.grid(row=0, column=0)

numberArea = tk.Entry(root) # This will take input through the window
numberArea.grid(row=0, column=1)


def convert():
    input_number = numberArea.get()
    output = float(input_number) * 2.71818 # Conversion formula
    result = tk.Label(root, text=f"{input_number}  converting to {output}")
    print(result) # This is optional but convenient. If any error appears on the window, it will be understood.
    result.grid(row=2, column=0, columnspan=2)

# Creating Button to convert
button = tk.Button(root, text="Convert", padx=10, pady=10, command=convert)
# command= will call a function, no () is needed, () will give an error
button.grid(row=1, column=0, columnspan=2, sticky='ew') # sticky='ew' will expand convert button east-west

# finally
root.mainloop()