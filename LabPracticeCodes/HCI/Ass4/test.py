import tkinter as tk
import random
from tkinter import simpledialog

class RedesignGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Redesign Tool")
        self.root.geometry("600x400")

        # Instruction Label
        self.instruction = tk.Label(self.root, text="Drag and Drop components to redesign the interface", font=("Arial", 12))
        self.instruction.pack(pady=10)

        # Left frame for components
        self.component_frame = tk.Frame(self.root, width=200, height=300, relief="sunken", bd=2)
        self.component_frame.place(x=10, y=50)

        # Create some GUI elements (Labels, Buttons, Entry)
        self.label_component = tk.Label(self.component_frame, text="Label", bg="lightblue")
        self.label_component.pack(pady=5)

        self.button_component = tk.Button(self.component_frame, text="Button", bg="lightgreen")
        self.button_component.pack(pady=5)

        self.entry_component = tk.Entry(self.component_frame)
        self.entry_component.pack(pady=5)

        # Main canvas for redesign
        self.canvas = tk.Canvas(self.root, bg="lightgray", width=350, height=300)
        self.canvas.place(x=230, y=50)

        # Binding drag and drop functionality to components
        self.label_component.bind("<Button-1>", self.on_click)
        self.button_component.bind("<Button-1>", self.on_click)
        self.entry_component.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_drop)

        # Variable to track the dragged widget
        self.dragged_widget = None

    def on_click(self, event):
        # Store the widget being dragged
        self.dragged_widget = event.widget

    def on_drag(self, event):
        # Move the widget to follow the mouse cursor
        if self.dragged_widget:
            x = event.x_root - self.dragged_widget.winfo_width() // 2
            y = event.y_root - self.dragged_widget.winfo_height() // 2
            self.dragged_widget.place(x=x, y=y)

    def on_drop(self, event):
        # Create a new instance of the dragged component on the canvas
        if self.dragged_widget:
            widget_type = self.dragged_widget.cget("text")

            # Create new widget based on the dragged component
            if widget_type == "Label":
                new_widget = tk.Label(self.canvas, text="New Label", bg="lightblue")
                new_widget.place(x=event.x, y=event.y)
                new_widget.bind("<Button-1>", self.rename_widget)
            elif widget_type == "Button":
                new_widget = tk.Button(self.canvas, text="New Button", bg="lightgreen")
                new_widget.place(x=event.x, y=event.y)
                new_widget.bind("<Button-1>", self.rename_widget)
            elif isinstance(self.dragged_widget, tk.Entry):
                random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                new_widget = tk.Entry(self.canvas, bg=random_color)
                new_widget.place(x=event.x, y=event.y)
                new_widget.bind("<Button-1>", self.rename_widget)

            # Reset dragged widget
            self.dragged_widget = None

    def rename_widget(self, event):
        # Prompt the user for a new name
        new_name = simpledialog.askstring("Rename", "Enter new name:")
        if new_name:
            event.widget.config(text=new_name)

if __name__ == "__main__":
    root = tk.Tk()
    gui = RedesignGUI(root)
    root.mainloop()
