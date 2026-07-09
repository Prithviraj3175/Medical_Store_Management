from tkinter import *
from tkinter import ttk, messagebox
import database

selected_id = None

# ---------------- Functions ----------------

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

def show():
    tree.delete(*tree.get_children())
    for row in database.view_medicines():
        tree.insert("", END, values=row)

def add():
    database.add_medicine(
        e1.get(),
        e2.get(),
        e3.get(),
        e4.get(),
        e5.get()
    )
    clear()
    show()
    messagebox.showinfo("Success", "Medicine Added Successfully")

def select_item(event):
    global selected_id

    selected = tree.focus()
    values = tree.item(selected, "values")

    if values:
        selected_id = values[0]

        clear()

        e1.insert(0, values[1])
        e2.insert(0, values[2])
        e3.insert(0, values[3])
        e4.insert(0, values[4])
        e5.insert(0, values[5])

def update():
    if selected_id:
        database.update_medicine(
            selected_id,
            e1.get(),
            e2.get(),
            e3.get(),
            e4.get(),
            e5.get()
        )
        clear()
        show()

def delete():
    if selected_id:
        database.delete_medicine(selected_id)
        clear()
        show()

# ---------------- GUI ----------------

root = Tk()
root.title("Medical Store Management System")
root.geometry("900x550")

Label(root, text="Medicine Name").place(x=20, y=20)
e1 = Entry(root, width=25)
e1.place(x=150, y=20)

Label(root, text="Category").place(x=20, y=60)
e2 = Entry(root, width=25)
e2.place(x=150, y=60)

Label(root, text="Price").place(x=20, y=100)
e3 = Entry(root, width=25)
e3.place(x=150, y=100)

Label(root, text="Stock").place(x=20, y=140)
e4 = Entry(root, width=25)
e4.place(x=150, y=140)

Label(root, text="Expiry Date").place(x=20, y=180)
e5 = Entry(root, width=25)
e5.place(x=150, y=180)

Button(root, text="Add", width=12, command=add).place(x=20, y=230)
Button(root, text="Update", width=12, command=update).place(x=140, y=230)
Button(root, text="Delete", width=12, command=delete).place(x=260, y=230)
Button(root, text="View All", width=12, command=show).place(x=380, y=230)
Button(root, text="Clear", width=12, command=clear).place(x=500, y=230)

columns = ("ID", "Medicine", "Category", "Price", "Stock", "Expiry")

tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130)

tree.place(x=20, y=290)

tree.bind("<ButtonRelease-1>", select_item)

show()

root.mainloop()