import tkinter as tk
from tkinter import messagebox

class RailwayTicketManagementSystem:
    def __init__(self, root):  # Corrected method name
        self.root = root
        self.root.title("Railway Ticket Management System")
        self.root.geometry("700x400")
        self.root.config(bg="#e0f7fa")

        self.booked_tickets = []
        # Title
        tk.Label(self.root, text="Railway Ticket Management System", font=("Arial", 18, "bold"), bg="#006064", fg="white").pack(pady=10)

        # Form Frame for Inputs
        form_frame = tk.Frame(self.root, bg="#e0f7fa")
        form_frame.pack(side=tk.LEFT, padx=20, pady=20)

        # Form Fields
        self.fields = {
            "Passenger Name": tk.StringVar(),
            "Train Number": tk.StringVar(),
            "Seat Number": tk.StringVar(),
            "Source": tk.StringVar(),
            "Destination": tk.StringVar()
        }
        
        row = 0
        for field, var in self.fields.items():
            tk.Label(form_frame, text=field, bg="#e0f7fa", fg="#006064", font=("Arial", 10, "bold")).grid(row=row, column=0, padx=10, pady=5)
            tk.Entry(form_frame, textvariable=var, bg="#ffffff", fg="#006064").grid(row=row, column=1, padx=10, pady=5)
            row += 1

        # Buttons Frame
        button_frame = tk.Frame(form_frame, bg="#e0f7fa")
        button_frame.grid(row=row, columnspan=2, pady=10)

        # Buttons
        tk.Button(button_frame, text="Book Ticket", command=self.book_ticket, bg="#004d40", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete All Bookings", command=self.delete_all_bookings, bg="#b71c1c", fg="white").pack(side=tk.LEFT, padx=5)

        # Listbox for Booked Tickets
        self.ticket_listbox = tk.Listbox(self.root, width=40, height=15, bg="#ffffff", fg="#006064", selectbackground="#b2dfdb", font=("Arial", 10))
        self.ticket_listbox.pack(side=tk.RIGHT, padx=20, pady=20)

    def book_ticket(self):
        # Collect ticket info from form fields
        info = {field: var.get() for field, var in self.fields.items()}

        if all(info.values()):  # Check if all fields are filled
            ticket_info = f"{info['Passenger Name']} | Train: {info['Train Number']} | Seat: {info['Seat Number']} | {info['Source']} -> {info['Destination']}"
            self.booked_tickets.append(ticket_info)
            self.ticket_listbox.insert(tk.END, ticket_info)  # Display in listbox
            self.clear_form()  # Clear form fields
            messagebox.showinfo("Success", "Ticket booked successfully!")
        else:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields.")

    def delete_all_bookings(self):
        if messagebox.askyesno("Delete All Bookings", "Are you sure you want to delete all bookings?"):
            self.booked_tickets.clear()
            self.ticket_listbox.delete(0, tk.END)
            messagebox.showinfo("Success", "All bookings deleted successfully.")

    def clear_form(self):
        for var in self.fields.values():
            var.set("")

# Main application
if __name__ == "__main__":  # Corrected condition
    root = tk.Tk()
    app = RailwayTicketManagementSystem(root)
    root.mainloop()
