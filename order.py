import sqlite3
from database import get_db


def add_order(menuid, quantity=1):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT price FROM menu WHERE menuid = ?", (menuid,))
    row = cursor.fetchone()
    if row is None:
        raise ValueError("Menu item not found")

    total = row[0] * quantity
    cursor.execute(
        "INSERT INTO orders (menuid, quantity, total) VALUES (?, ?, ?)",
        (menuid, quantity, total),
    )
    conn.commit()
    return cursor.lastrowid
