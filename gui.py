import tkinter as tk
from tkinter import ttk
from db import create_table,add_transaction,view_trans,summary,plot_summary

create_table()
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x550")

# --- إدخالات المستخدم ---

# نوع العملية (دخل أو مصروف)
tk.Label(root, text="Type (income/expense):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
type_var = tk.StringVar()
type_box = ttk.Combobox(root, textvariable=type_var, values=["income", "expense"])
type_box.grid(row=0, column=1, padx=5, pady=5)

# المبلغ
tk.Label(root, text="Amount:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# الفئة
tk.Label(root, text="Category:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=2, column=1, padx=5, pady=5)

# التاريخ
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1, padx=5, pady=5)

# الوصف
tk.Label(root, text="Description:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
desc_entry = tk.Entry(root)
desc_entry.grid(row=4, column=1, padx=5, pady=5)

# --- زر الإضافة ---
def add_transaction_gui():
    try:
        t = type_var.get()
        a = float(amount_entry.get())
        c = category_entry.get()
        d = date_entry.get()
        desc = desc_entry.get()
        add_transaction(t, a, c, d, desc)
        status_label.config(text="✅ Transaction added!")
        refresh_table()
    except:
        status_label.config(text="⚠️ Please fill all fields correctly")

add_btn = tk.Button(root, text="Add Transaction", command=add_transaction_gui)
add_btn.grid(row=5, column=0, columnspan=2, pady=10)

# --- جدول عرض المعاملات ---
tree = ttk.Treeview(root, columns=("ID", "Type", "Amount", "Category", "Date", "Description"), show="headings")
tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# إعداد رؤوس الأعمدة
for col in tree["columns"]:
    tree.heading(col, text=col)

# تحديث الجدول بالبيانات
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    rows = view_trans(return_data=True)
    for row in rows:
        tree.insert("", tk.END, values=row)

refresh_table()

# --- عرض الملخص داخل النافذة ---
def show_summary():
    income, expense = summary()
    balance = income - expense
    summary_text = f"💰 Income: {income}\n💸 Expense: {expense}\n🧾 Balance: {balance}"
    summary_label.config(text=summary_text)

summary_btn = tk.Button(root, text="Show Summary", command=show_summary)
summary_btn.grid(row=7, column=0, pady=10)

summary_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
summary_label.grid(row=8, column=0, columnspan=2)

# --- زر رسم بياني ---
chart_btn = tk.Button(root, text="Show Chart", command=plot_summary)
chart_btn.grid(row=7, column=1, pady=10)

# --- رسالة الحالة ---
status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=9, column=0, columnspan=2)

# تشغيل البرنامج
root.mainloop()
