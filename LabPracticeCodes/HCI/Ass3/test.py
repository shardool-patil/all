import tkinter as tk

def change_color(color):
    root.config(bg=color)

# Create the main window
root = tk.Tk()
root.title("Color Change GUI")
root.geometry("300x200")

# Create buttons with different colors
button_red = tk.Button(root, text="Red", command=lambda: change_color("red"))
button_red.pack(pady=10)

button_green = tk.Button(root, text="Green", command=lambda: change_color("green"))
button_green.pack(pady=10)

button_blue = tk.Button(root, text="Blue", command=lambda: change_color("blue"))
button_blue.pack(pady=10)

button_default = tk.Button(root, text="Default", command=lambda: change_color("SystemButtonFace"))
button_default.pack(pady=10)

# Run the application
root.mainloop()