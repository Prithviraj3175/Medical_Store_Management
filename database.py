import sqlite3

# Database Connection
conn = sqlite3.connect("medical.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS medicine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medicine_name TEXT,
    category TEXT,
    price INTEGER,
    stock INTEGER,
    expiry_date TEXT
)
""")
conn.commit()

# Add Medicine
def add_medicine(medicine_name, category, price, stock, expiry_date):
    cursor.execute(
        "INSERT INTO medicine(medicine_name, category, price, stock, expiry_date) VALUES (?, ?, ?, ?, ?)",
        (medicine_name, category, price, stock, expiry_date)
    )
    conn.commit()

# View All Medicines
def view_medicines():
    cursor.execute("SELECT * FROM medicine")
    return cursor.fetchall()

# Search Medicine
def search_medicine(medicine_name):
    cursor.execute("SELECT * FROM medicine WHERE medicine_name=?", (medicine_name,))
    return cursor.fetchall()

# Update Medicine
def update_medicine(id, medicine_name, category, price, stock, expiry_date):
    cursor.execute("""
        UPDATE medicine
        SET medicine_name=?, category=?, price=?, stock=?, expiry_date=?
        WHERE id=?
    """, (medicine_name, category, price, stock, expiry_date, id))
    conn.commit()

# Delete Medicine
def delete_medicine(id):
    cursor.execute("DELETE FROM medicine WHERE id=?", (id,))
    conn.commit()

# Close Database
def close():
    conn.close()