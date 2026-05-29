from tkinter import *
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
training_data = [
    ("Pizza", "Food"),
    ("Burger", "Food"),
    ("Restaurant", "Food"),
    ("Bus", "Travel"),
    ("Train", "Travel"),
    ("Uber", "Travel"),
    ("Electricity", "Bills"),
    ("Water Bill", "Bills"),
    ("Shopping Mall", "Shopping"),
    ("Clothes", "Shopping"),
]


texts = [x[0] for x in training_data]
labels = [x[1] for x in training_data]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X, labels)

def predict_category():

    description = description_entry.get()

    if description == "":
        return

    transformed = vectorizer.transform([description])

    prediction = knn.predict(transformed)
    print(prediction)
    category_combo.set(prediction[0])

FILE_NAME = "expenses.csv"

# ---------------- SAVE CSV ----------------
def save_all_data():

    with open(FILE_NAME, mode="w", newline="") as file:

        writer = csv.writer(file)

        for item in table.get_children():

            row = table.item(item)['values']

            writer.writerow(row)

    calculate_total()


# ---------------- ADD EXPENSE ----------------
def add_expense():

    date = date_entry.get()
    category = category_combo.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if date == "" or category == "" or amount == "":
        messagebox.showerror("Error", "Please fill all required fields")
        return

    table.insert(
        "",
        END,
        values=(date, category, amount, description)
    )

    save_all_data()

    clear_fields()


# ---------------- LOAD DATA ----------------
def load_data():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, mode="r") as file:

            reader = csv.reader(file)

            for row in reader:
                table.insert("", END, values=row)

    calculate_total()


# ---------------- CLEAR FIELDS ----------------
def clear_fields():

    date_entry.delete(0, END)
    date_entry.insert(0, datetime.now().strftime("%d-%m-%Y"))

    category_combo.set("")

    amount_entry.delete(0, END)

    description_entry.delete(0, END)


# ---------------- SELECT RECORD ----------------
def select_record(event):

    selected = table.focus()

    values = table.item(selected, 'values')

    if values:

        clear_fields()

        date_entry.delete(0, END)
        date_entry.insert(0, values[0])

        category_combo.set(values[1])

        amount_entry.insert(0, values[2])

        description_entry.insert(0, values[3])


# ---------------- UPDATE EXPENSE ----------------
def update_expense():

    selected = table.focus()

    if not selected:
        return

    table.item(
        selected,
        values=(
            date_entry.get(),
            category_combo.get(),
            amount_entry.get(),
            description_entry.get()
        )
    )

    save_all_data()

    clear_fields()


# ---------------- DELETE EXPENSE ----------------
def delete_expense():

    selected = table.focus()

    if not selected:
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete?"
    )

    if confirm:

        table.delete(selected)

        save_all_data()

        clear_fields()


# ---------------- TOTAL CALCULATION ----------------
def calculate_total():

    total = 0

    for item in table.get_children():

        values = table.item(item)['values']

        total += float(values[2])

    total_label.config(text=f"Total Expense: ₹ {total}")


# ---------------- SEARCH FUNCTION ----------------
def search_expense():

    search_text = search_entry.get().lower()

    for item in table.get_children():

        table.delete(item)

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, mode="r") as file:

            reader = csv.reader(file)

            for row in reader:

                row_text = " ".join(row).lower()

                if search_text in row_text:

                    table.insert("", END, values=row)

    calculate_total()


# ---------------- RESET SEARCH ----------------
def reset_search():

    for item in table.get_children():
        table.delete(item)

    load_data()


# ---------------- WINDOW ----------------
root = Tk()

root.title("Expense Manager")

root.geometry("900x600")

root.configure(bg="white")


# ---------------- TITLE ----------------
title = Label(
    root,
    text="Expense Manager",
    font=("Arial", 20, "bold"),
    bg="white"
)

title.pack(pady=10)


# ---------------- FORM FRAME ----------------
form_frame = Frame(root, bg="white")

form_frame.pack(pady=10)


# DATE
Label(
    form_frame,
    text="Date",
    bg="white"
).grid(row=0, column=0, padx=10, pady=5)

date_entry = Entry(form_frame, width=20)

date_entry.grid(row=0, column=1)

date_entry.insert(0, datetime.now().strftime("%d-%m-%Y"))


# CATEGORY
Label(
    form_frame,
    text="Category",
    bg="white"
).grid(row=1, column=0, padx=10, pady=5)

category_combo = ttk.Combobox(
    form_frame,
    values=[
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Entertainment",
        "Medical",
        "Education"
    ],
    width=18
)

category_combo.grid(row=1, column=1)


# AMOUNT
Label(
    form_frame,
    text="Amount",
    bg="white"
).grid(row=2, column=0, padx=10, pady=5)

amount_entry = Entry(form_frame, width=20)

amount_entry.grid(row=2, column=1)


# DESCRIPTION
Label(
    form_frame,
    text="Description",
    bg="white"
).grid(row=3, column=0, padx=10, pady=5)

description_entry = Entry(form_frame, width=20)

description_entry.grid(row=3, column=1)


# ---------------- BUTTONS ----------------
button_frame = Frame(root, bg="white")

button_frame.pack(pady=10)

Button(
    button_frame,
    text="Add Expense",
    width=15,
    bg="green",
    fg="white",
    command=add_expense
).grid(row=0, column=0, padx=5)

Button(
    button_frame,
    text="Update",
    width=15,
    bg="blue",
    fg="white",
    command=update_expense
).grid(row=0, column=1, padx=5)

Button(
    button_frame,
    text="Delete",
    width=15,
    bg="red",
    fg="white",
    command=delete_expense
).grid(row=0, column=2, padx=5)

Button(
    button_frame,
    text="Predict Category",
    width=15,
    bg="purple",
    fg="white",
    command=predict_category
).grid(row=0, column=3, padx=5)

# ---------------- SEARCH ----------------
search_frame = Frame(root, bg="white")

search_frame.pack(pady=10)

search_entry = Entry(search_frame, width=30)

search_entry.grid(row=0, column=0, padx=5)

Button(
    search_frame,
    text="Search",
    command=search_expense
).grid(row=0, column=1, padx=5)

Button(
    search_frame,
    text="Reset",
    command=reset_search
).grid(row=0, column=2, padx=5)


# ---------------- TABLE ----------------
table = ttk.Treeview(
    root,
    columns=("Date", "Category", "Amount", "Description"),
    show="headings",
    height=15
)

table.heading("Date", text="Date")
table.heading("Category", text="Category")
table.heading("Amount", text="Amount")
table.heading("Description", text="Description")

table.column("Date", width=120)
table.column("Category", width=150)
table.column("Amount", width=100)
table.column("Description", width=300)

table.pack(pady=20)

table.bind("<ButtonRelease-1>", select_record)


# ---------------- TOTAL LABEL ----------------
total_label = Label(
    root,
    text="Total Expense: ₹ 0",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="darkgreen"
)

total_label.pack(pady=10)


# ---------------- LOAD DATA ----------------
load_data()


# ---------------- RUN APP ----------------
root.mainloop()