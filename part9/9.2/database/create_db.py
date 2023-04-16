import sqlite3
from sqlite3 import Cursor

from database import DB_NAME


def create_db(set_mock_data: bool = True) -> None:
    # Создаем подключение к базе данных
    conn = sqlite3.connect(DB_NAME)

    # Создаем курсор для работы с базой данных
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS pizza (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        description TEXT,
                        price REAL
                    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        phone TEXT,
                        address TEXT,
                        is_completed INTEGER DEFAULT 0
                    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS order_item (
                        id INTEGER PRIMARY KEY,
                        pizza_id INTEGER,
                        order_id INTEGER,
                        quantity INTEGER,
                        FOREIGN KEY(pizza_id) REFERENCES pizza(id),
                        FOREIGN KEY(order_id) REFERENCES orders(id)
                    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS employee (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        position TEXT
                    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS shift (
                        id INTEGER PRIMARY KEY,
                        employee_id INTEGER,
                        start_time TEXT,
                        end_time TEXT,
                        FOREIGN KEY(employee_id) REFERENCES employee(id)
                    )''')

    if set_mock_data:
        insert_mock_data(cur)
        conn.commit()

    cur.close()
    conn.close()


def insert_mock_data(cur: Cursor) -> None:
    pizzas = [
        ("Margherita", "Tomato sauce, mozzarella, basil", 10.99),
        ("Pepperoni", "Tomato sauce, mozzarella, pepperoni", 12.99),
        ("Hawaiian", "Tomato sauce, mozzarella, ham, pineapple", 11.99),
        ("Meat Feast", "Tomato sauce, mozzarella, sausage, bacon, pepperoni", 15.99),
    ]

    orders = [
        ("John Smith", "(555) 555-1212", "123 Main St, Anytown, USA"),
        ("Jane Doe", "(555) 555-1313", "456 Elm St, Anytown, USA"),
    ]

    order_items = [
        (1, 1, 2),
        (2, 1, 1),
        (4, 2, 3),
    ]

    employees = [
        ("David Johnson", "Manager"),
        ("Sarah Lee", "Chef"),
        ("Mark Smith", "Waiter"),
    ]

    shifts = [
        (1, "09:00", "17:00"),
        (2, "10:00", "18:00"),
        (3, "12:00", "20:00"),
    ]

    cur.executemany("INSERT INTO pizza (name, description, price) VALUES (?, ?, ?)", pizzas)
    cur.executemany("INSERT INTO orders (name, phone, address) VALUES (?, ?, ?)", orders)
    cur.executemany("INSERT INTO order_item (pizza_id, order_id, quantity) VALUES (?, ?, ?)", order_items)
    cur.executemany("INSERT INTO employee (name, position) VALUES (?, ?)", employees)
    cur.executemany("INSERT INTO shift (employee_id, start_time, end_time) VALUES (?, ?, ?)", shifts)
