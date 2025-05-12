import tkinter as tk
from tkinter import messagebox
import pyqrcode
from PIL import Image, ImageTk

def generate_qr():
    # Get user input
    text = entry.get()
    # In case user forget to input:
    if not text.strip():
        messagebox.showerror("Error", "Input text cannot be empty!")
        return

    # Generate QR code
    qr = pyqrcode.create(text)
    qr.png("qr_code.png", scale=8)

    # Display the QR code on the window
    img = Image.open("qr_code.png")
    img = ImageTk.PhotoImage(img)

    # Update the label to display the image
    qr_label.config(image=img)
    qr_label.image = img  # Prevent garbage collection

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")

# Create a text entry widget
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Create a button to trigger the QR code generation
generate_button = tk.Button(root, text="Generate", command=generate_qr, font=("Arial", 14))
generate_button.pack(pady=10)

# Create a label to display the generated QR code
qr_label = tk.Label(root)
qr_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
