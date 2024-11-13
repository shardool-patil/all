import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class FileUploadGOMS:
    def __init__(self, master):
        self.master = master
        self.master.title("File Upload Simulation")
        self.master.geometry("400x200")

        # Create buttons for file selection and upload
        self.choose_file_button = tk.Button(master, text="Choose File", command=self.choose_file)
        self.choose_file_button.pack(pady=20)

        self.upload_button = tk.Button(master, text="Upload File", state=tk.DISABLED, command=self.upload_file)
        self.upload_button.pack(pady=10)

        self.file_path = None

    # Operator 1: Choose File
    def choose_file(self):
        self.file_path = filedialog.askopenfilename(title="Select a File")
        if self.file_path:
            self.upload_button.config(state=tk.NORMAL)  # Enable upload button
            print("Operator: File selected at path:", self.file_path)
        else:
            print("Operator: No file selected.")

    # Operator 2: Upload File
    def upload_file(self):
        if self.file_path:
            self.wait_for_upload()
            self.confirm_upload()
            print("Goal: File uploaded successfully!")
        else:
            messagebox.showwarning("No File", "Please select a file before uploading.")
    
    # Method: Wait for the upload process to complete
    def wait_for_upload(self):
        print("Operator: Waiting for the upload to complete...")
        # Simulating the wait for upload process (e.g., using sleep or progress bar)
        # For now, just simulate it.
        
    # Method: Confirm the file upload
    def confirm_upload(self):
        messagebox.showinfo("Upload Success", "File uploaded successfully!")
        print("Operator: Upload confirmation received.")

def main():
    root = tk.Tk()
    app = FileUploadGOMS(root)
    root.mainloop()

if __name__ == "__main__":
    main()
