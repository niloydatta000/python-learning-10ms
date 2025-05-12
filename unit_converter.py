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

root = tk.Tk()
root.title("Unit Converter")

unitsData = {
    'mm' : 0.1,
    'cm' : 1, # base value
    'm' : 100,
    'km' : 100000,
    'inch' : 2.54,
    'ft' : 30.48,
    'yard' : 91.44,
    'mile' : 160934
}

# Now set entry box & take input
inputArea = tk.Entry(root)
inputArea.grid(row=0, column=0)

def convertUnit(fromUnit, toUnit, length):
    # In case user forget to select units:
    if fromUnit not in unitsData or toUnit not in unitsData:
        resultLabel.config(text="Please select units")
        return
    # In case user forget to enter value:
    try:
        length = float(length)
    except ValueError:
        resultLabel.config(text="Please enter a valid value")
        return

    result = float(length) * (unitsData[fromUnit] / unitsData[toUnit])
    print(result) # This is optional but convenient. If any error appears on the window, it will be understood.
    '''
    We are adding config() instead of grid() to avoid overlapping.
    We will add grid() later otherwise previous results will overlap with new results.
    config() will reconfigure result each time so that previous results won't interrupt.
    '''
    # Calling resultLabel to configure
    resultLabel.config(text=f"{length} {fromUnit} = {result} {toUnit}")


selectFromUnit = tk.StringVar(root)
selectFromUnit.set("Select unit")
fromUnitSelectBox = tk.OptionMenu(root, selectFromUnit, *unitsData.keys())
fromUnitSelectBox.grid(row=0, column=1)

toTextLabel = tk.Label(root, text="Select an Unit", padx=5, pady=5)
toTextLabel.grid(row=1, column=0)

selectToUnit = tk.StringVar(root)
selectToUnit.set("Select unit")
toUnitSelectBox = tk.OptionMenu(root, selectToUnit, *unitsData.keys())
toUnitSelectBox.grid(row=1, column=1)

# Create Button to convert Inputted Data
convertButton = tk.Button(
    root,
    text = "Convert",
    padx = 4,
    pady = 3,
    # to put parameter on command, lambda keyword must be called then put colon(:) and function name
    command = lambda : convertUnit(
        selectFromUnit.get(),
        selectToUnit.get(),
        inputArea.get()
    )
)
convertButton.grid(row=2, column=0, columnspan=2, sticky='ew')

# Initializing result
resultLabel = tk.Label(root, text="Press Convert", padx=4, pady=4)
resultLabel.grid(row=3,column=0, columnspan=2)

# finally
root.mainloop()