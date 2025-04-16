import tkinter as tk
from tkinter import messagebox, simpledialog

customers = {}
products = {}
bills = []

# Functions
def add_customer():
    name = simpledialog.askstring("Add Customer", "Enter customer name:")
    if not name:
        return
    if name in customers:
        messagebox.showwarning("Warning", "Customer already exists.")
    else:
        customers[name] = []
        messagebox.showinfo("Success", f"Customer '{name}' added.")

def add_product():
    name = simpledialog.askstring("Add Product", "Enter product name:")
    if not name:
        return
    if name in products:
        messagebox.showwarning("Warning", "Product already exists.")
        return
    try:
        price = float(simpledialog.askstring("Add Product", "Enter product price:"))
        products[name] = price
        messagebox.showinfo("Success", f"Product '{name}' added at ₹{price}.")
    except:
        messagebox.showerror("Error", "Invalid price.")

def create_bill():
    name = simpledialog.askstring("Create Bill", "Enter customer name:")
    if name not in customers:
        messagebox.showerror("Error", "Customer not found.")
        return
    
    bill = {"customer": name, "items": [], "total": 0}
    
    while True:
        product_name = simpledialog.askstring("Create Bill", "Enter product name (or type 'done'):")
        if product_name == 'done':
            break
        if product_name not in products:
            messagebox.showwarning("Warning", "Product not found.")
            continue
        try:
            quantity = int(simpledialog.askstring("Create Bill", f"Enter quantity of '{product_name}':"))
            item_total = quantity * products[product_name]
            bill["items"].append({"product": product_name, "quantity": quantity, "total": item_total})
            bill["total"] += item_total
        except:
            messagebox.showerror("Error", "Invalid quantity.")
    
    if bill["items"]:
        customers[name].append(bill)
        bills.append(bill)
        messagebox.showinfo("Bill Created", f"Bill created successfully.\nTotal: ₹{bill['total']}")

def view_bills():
    name = simpledialog.askstring("View Bills", "Enter customer name:")
    if name not in customers:
        messagebox.showerror("Error", "Customer not found.")
        return
    
    bill_text = ""
    for i, bill in enumerate(customers[name]):
        bill_text += f"\nBill ID: {i + 1}, Total: ₹{bill['total']}\n"
        for item in bill['items']:
            bill_text += f"  {item['product']} x{item['quantity']} - ₹{item['total']}\n"
    
    if not bill_text:
        bill_text = "No bills found for this customer."
    
    messagebox.showinfo(f"{name}'s Bills", bill_text)

# Main GUI window
root = tk.Tk()
root.title("Billing Management System")
root.geometry("400x300")
root.resizable(False, False)

# GUI layout
title = tk.Label(root, text="Billing Management System", font=("Arial", 16, "bold"))
title.pack(pady=10)

btn1 = tk.Button(root, text="Add Customer", width=25, command=add_customer)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Add Product", width=25, command=add_product)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Create Bill", width=25, command=create_bill)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="View Customer's Bills", width=25, command=view_bills)
btn4.pack(pady=5)

btn5 = tk.Button(root, text="Exit", width=25, command=root.quit)
btn5.pack(pady=20)

root.mainloop()
