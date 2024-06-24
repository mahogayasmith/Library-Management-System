import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mahoga@1234',
        database='library_db'
    )
    return connection

def add_book(title, author, quantity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)", (title, author, quantity))
    conn.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo("Success", "Book added successfully!")

def remove_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo("Success", "Book removed successfully!")

def view_stock():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    
    stock_window = tk.Toplevel()
    stock_window.title("Book Stock")
    stock_window.configure(bg="#f0f0f0")
    
    columns = ('id', 'title', 'author', 'quantity')
    tree = ttk.Treeview(stock_window, columns=columns, show='headings')
    
    tree.heading('id', text='ID')
    tree.heading('title', text='Title')
    tree.heading('author', text='Author')
    tree.heading('quantity', text='Quantity')
    
    for book in books:
        tree.insert('', tk.END, values=book)
    
    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    cursor.close()
    conn.close()

def open_add_book_window():
    add_window = tk.Toplevel()
    add_window.title("Add Book")
    add_window.configure(bg="#f0f0f0")

    tk.Label(add_window, text="Title", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    title_entry = tk.Entry(add_window, font=("Arial", 12))
    title_entry.pack(pady=5)

    tk.Label(add_window, text="Author", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    author_entry = tk.Entry(add_window, font=("Arial", 12))
    author_entry.pack(pady=5)

    tk.Label(add_window, text="Quantity", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    quantity_entry = tk.Entry(add_window, font=("Arial", 12))
    quantity_entry.pack(pady=5)

    def submit_add_book():
        title = title_entry.get()
        author = author_entry.get()
        quantity = int(quantity_entry.get())
        add_book(title, author, quantity)
        add_window.destroy()

    tk.Button(add_window, text="Add Book", command=submit_add_book, bg="#0078d7", fg="white", font=("Arial", 12)).pack(pady=10)

def open_remove_book_window():
    remove_window = tk.Toplevel()
    remove_window.title("Remove Book")
    remove_window.configure(bg="#f0f0f0")

    tk.Label(remove_window, text="Book ID", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    book_id_entry = tk.Entry(remove_window, font=("Arial", 12))
    book_id_entry.pack(pady=5)

    def submit_remove_book():
        book_id = int(book_id_entry.get())
        remove_book(book_id)
        remove_window.destroy()

    tk.Button(remove_window, text="Remove Book", command=submit_remove_book, bg="#0078d7", fg="white", font=("Arial", 12)).pack(pady=10)

# Main window
root = tk.Tk()
root.title("Library Management System")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Library Management System", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

tk.Button(root, text="Add Book", command=open_add_book_window, bg="#0078d7", fg="white", font=("Arial", 14), width=20).pack(pady=10)
tk.Button(root, text="Remove Book", command=open_remove_book_window, bg="#0078d7", fg="white", font=("Arial", 14), width=20).pack(pady=10)
tk.Button(root, text="View Stock", command=view_stock, bg="#0078d7", fg="white", font=("Arial", 14), width=20).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit, bg="#0078d7", fg="white", font=("Arial", 14), width=20).pack(pady=10)

root.mainloop()
