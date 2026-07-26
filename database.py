import sqlite3


def create_connection():
    return sqlite3.connect("ByteBean.db")


def create_table():

    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            category TEXT,
            drink TEXT,
            price REAL,
            quantity INTEGER,
            total REAL
        )
    """)

    connection.commit()

    connection.close()

def insert_order(
    customer_name,
    category,
    drink,
    price,
    quantity,
    total
):
    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO Orders (
        customer_name,
        category,
        drink,
        price,
        quantity,
        total
    )
    VALUES (?, ?, ?, ?, ?, ?)
""", (
    customer_name,
    category,
    drink,
    price,
    quantity,
    total
))

    connection.commit()
    connection.close()

def view_orders():
        connection = create_connection()

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Orders")

        orders = cursor.fetchall()

        connection.close()

        return orders


def search_orders_by_customer(customer_name):
     connection = create_connection()

     cursor = connection.cursor()

     cursor.execute("SELECT * FROM Orders WHERE customer_name = ?", (customer_name,))

     orders = cursor.fetchall()

     connection.close()

     return orders


def update_order(order_id,customer_name,category,drink,price,quantity,total):

     connection= create_connection()
     cursor = connection.cursor()

     cursor.execute("""
     UPDATE Orders
     SET
     customer_name = ?,
      category = ?,
    drink = ?,
    price = ?,
    quantity = ?,
    total = ?
WHERE id = ?
""", (
    customer_name,
    category,
    drink,
    price,
    quantity,
    total,
    order_id
))
     
     connection.commit()
     connection.close()



def delete_order(order_id):

     connection = create_connection()

     cursor= connection.cursor()

     cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))

     connection.commit()
     connection.close()

     