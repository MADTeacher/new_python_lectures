import sqlite3

from database import DB_NAME


def add_order(name: str, phone: str, address: str) -> int:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("INSERT INTO orders (name, phone, address) VALUES (?, ?, ?)",
                    (name, phone, address))
        conn.commit()
        return cur.lastrowid


def add_order_item(pizza_id: int, order_id: int, quantity: int) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("INSERT INTO order_item (pizza_id, order_id, quantity) VALUES (?, ?, ?)",
                    (pizza_id, order_id, quantity))
        conn.commit()


def set_completed_order(order_id: int) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("UPDATE orders SET is_completed = 1 WHERE id = ?", (order_id,))
        conn.commit()


def get_completed_orders() -> list:
    return __get_orders_with_status(1)


def get_current_orders() -> list:
    return __get_orders_with_status(0)


def __get_orders_with_status(status: int) -> list:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("SELECT * FROM orders WHERE is_completed = ?", (status,))
        rows = cur.fetchall()
        return rows


def get_orders() -> list:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("SELECT * FROM orders")
        rows = cur.fetchall()
        return rows


def get_orders_with_pizzas(order_id: int) -> list:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute('''SELECT orders.id, orders.is_completed, orders.name, orders.phone, orders.address, pizza.name, order_item.quantity 
                       FROM orders 
                       JOIN order_item ON orders.id = order_item.order_id 
                       JOIN pizza ON order_item.pizza_id = pizza.id
                       WHERE orders.id = ?''', (order_id,))

        results = cur.fetchall()
        return results
