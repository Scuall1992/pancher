import tkinter as tk
from tkinter import filedialog

def upload_action():
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def download_action():
    # Dummy action for download
    print('Download action triggered')

root = tk.Tk()
root.title("File Management GUI")

# Set the size of the window to match the image reference
root.geometry("800x600")

# Create a listbox to represent the "List of cases"
listbox = tk.Listbox(root)
listbox.place(x=50, y=50, width=300, height=500)

# Add a label for the listbox
label = tk.Label(root, text="List of cases")
label.place(x=50, y=20)

# Create the "Upload file" button
upload_button = tk.Button(root, text="Button Upload file", command=upload_action)
upload_button.place(x=400, y=200, width=150, height=50)

# Create the "Download File" button
download_button = tk.Button(root, text="Button Download File", command=download_action)
download_button.place(x=400, y=300, width=150, height=50)

# Run the application
root.mainloop()
