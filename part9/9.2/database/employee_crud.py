import sqlite3

from database import DB_NAME


def add_employee(name: str, position: str) -> int:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("INSERT INTO employee (name, position) VALUES (?, ?)",
                    (name, position))
        conn.commit()
        return cur.lastrowid


def add_shift(employee_id: int, start_time: str, end_time: str) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("INSERT INTO shift (employee_id, start_time, end_time) VALUES (?, ?, ?)",
                    (employee_id, start_time, end_time))
        conn.commit()


def delete_employee(employee_id: int) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("DELETE FROM employee WHERE id = ?", (employee_id,))
        conn.commit()


def delete_shift(employee_id: int) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("DELETE FROM shift WHERE employee_id = ?", (employee_id,))
        conn.commit()


def get_employees() -> list:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("SELECT * FROM employee")
        rows = cur.fetchall()
        return rows


def get_shifts() -> list:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute("SELECT * FROM shift")
        rows = cur.fetchall()
        return rows


def get_employees_with_shifts() -> list:
    with sqlite3.connect(DB_NAME) as conn:
        cur: sqlite3.Cursor = conn.cursor()
        cur.execute('''SELECT employee.id, employee.name, employee.position, shift.start_time, shift.end_time
                       FROM employee 
                       JOIN shift ON employee.id = shift.employee_id''')

        results = cur.fetchall()
        return results
