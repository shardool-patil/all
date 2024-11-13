import tkinter as tk
from tkinter import messagebox

class RailwayReservation:
    def __init__(self, master):
        self.master = master
        self.master.title("Railway Reservation System")
        self.master.geometry("400x300")

        # Labels and Entry fields
        tk.Label(master, text="Train Name:").grid(row=0, column=0, padx=10, pady=10)
        self.train_name = tk.Entry(master)
        self.train_name.grid(row=0, column=1)

        tk.Label(master, text="Source Station:").grid(row=1, column=0, padx=10, pady=10)
        self.source_station = tk.Entry(master)
        self.source_station.grid(row=1, column=1)

        tk.Label(master, text="Destination Station:").grid(row=2, column=0, padx=10, pady=10)
        self.dest_station = tk.Entry(master)
        self.dest_station.grid(row=2, column=1)

        tk.Label(master, text="Passenger Name:").grid(row=3, column=0, padx=10, pady=10)
        self.passenger_name = tk.Entry(master)
        self.passenger_name.grid(row=3, column=1)

        tk.Label(master, text="Age:").grid(row=4, column=0, padx=10, pady=10)
        self.age = tk.Entry(master)
        self.age.grid(row=4, column=1)

        # Book Ticket Button
        self.book_button = tk.Button(master, text="Book Ticket", command=self.book_ticket)
        self.book_button.grid(row=5, column=0, columnspan=2, pady=20)

    def book_ticket(self):
        if (self.train_name.get() and self.source_station.get() and self.dest_station.get() and
                self.passenger_name.get() and self.age.get()):
            messagebox.showinfo("Booking Confirmation", "Ticket Booked Successfully!")
        else:
            messagebox.showwarning("Missing Information", "Please fill in all fields.")

# Initialize the GUI
root = tk.Tk()
app = RailwayReservation(root)
root.mainloop()
