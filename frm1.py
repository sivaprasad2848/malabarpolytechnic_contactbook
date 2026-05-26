from tkinter import *

# Function to display entered data
def submit_data():
    name = name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()

    print("Name :", name)
    print("Email :", email)
    print("Mobile :", mobile)


# Create window
root = Tk()
root.title("User Form")
root.geometry("300x250")

# Name
Label(root, text="Name").pack(pady=5)
name_entry = Entry(root, width=30)
name_entry.pack()

# Email
Label(root, text="Email").pack(pady=5)
email_entry = Entry(root, width=30)
email_entry.pack()

# Mobile
Label(root, text="Mobile").pack(pady=5)
mobile_entry = Entry(root, width=30)
mobile_entry.pack()

# Button
Button(root, text="Submit", command=submit_data).pack(pady=20)

# Run window
root.mainloop()