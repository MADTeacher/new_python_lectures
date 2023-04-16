import sqlite3

from database import DB_NAME


def add_pizza(name: str, description: str, price: float) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("INSERT INTO pizza (name, description, price) VALUES (?, ?, ?)",
                    (name, description, price))
        conn.commit()


def delete_pizza(pizza_id: int) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("DELETE FROM pizza WHERE id = ?", (pizza_id,))
        conn.commit()


def get_pizzas() -> list:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("SELECT * FROM pizza")
        rows = cur.fetchall()
        return rows


def get_pizzas_by_price(max_price: float) -> list:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute('''SELECT *
                           FROM pizza
                           WHERE price >= ?''', (max_price,))

        results = cur.fetchall()
        return results


def get_sort_pizzas_by_price() -> list:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute('''SELECT *
                           FROM pizza
                           ORDER BY price''')

        results = cur.fetchall()
        return results


def change_pizza_name(pizza_id: int, new_name: str) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("UPDATE pizza SET name = ? WHERE id = ?", (new_name, pizza_id))
        conn.commit()


def change_pizza_description(pizza_id: int, new_description: str) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("UPDATE pizza SET description = ? WHERE id = ?", (new_description, pizza_id))
        conn.commit()


def change_pizza_price(pizza_id: int, new_price: float) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("UPDATE pizza SET price = ? WHERE id = ?", (new_price, pizza_id))
        conn.commit()
