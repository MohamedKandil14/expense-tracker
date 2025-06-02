import sqlite3
import matplotlib.pyplot as plt

def create_connection():
    conn = sqlite3.connect("expenses.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            date TEXT NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()
 
"""------------------------------------------------------------------------"""
def add_transaction(type,amount,category,date,description):
        conn=create_connection()
        cursor=conn.cursor()
        cursor.execute("""
        INSERT INTO  transactions (type,amount,category,date,description)Values(?,?,?,?,?)""",(type,amount,category,date,description))
        conn.commit()
        conn.close()

def view_trans(return_data=False):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = cursor.fetchall()

    conn.close()

    if return_data:
        return rows
    else:
        for row in rows:
            print(row)


"""---------------------------------------------------------------"""
def view_trans_by_date(start_date,end_date):
     conn=create_connection()
     cursor=conn.cursor()
     cursor.execute("""
            select * from transactions
            where date between ? and ?
            order by date asc

""",(start_date,end_date))
     rows=cursor.fetchall()
     for row in rows:
          print(row)
     conn.close()
"""------------------------------------------------------------------------"""
def summary():
     conn=create_connection()
     cursor=conn.cursor()
     cursor.execute("""
select sum(amount) from transactions where type='income'""")
     income=cursor.fetchone()[0] or 0
     cursor.execute("""
select sum(amount) from transactions where type='expense'""")
     expense=cursor.fetchone()[0] or 0
     balance=income-expense
     print(f"total income {income}")
     print(f"total expense {expense}")
     print(f"Balance {balance}")
     conn.close()
"""--------------------------------------------------------------------------"""
def plot_summary():
     conn=create_connection()
     cursor=conn.cursor()
     cursor.execute(""" select type,sum(amount) from transactions group by type  """)
     data=cursor.fetchall()
     labels=[row[0]for row in data]
     values=[row[1]for row in data]
     plt.pie(values,labels=labels,autopct='%1.1f%%',startangle=140)
     plt.title("income vs expense")
     plt.axis('equal')
     plt.show()
     conn.close()
     