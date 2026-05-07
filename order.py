import sqlite3
from database import get_db


def add_order(menuid, quantity=1):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT price FROM menu WHERE menuid = ?", (menuid,))
    row = cursor.fetchone()
    if row is None:
        raise ValueError("Menu item not found")

    price = row[0]
    cursor.execute("SELECT orderid, quantity FROM orders WHERE menuid = ?", (menuid,))
    existing_order = cursor.fetchone()

    if existing_order:
        orderid, existing_quantity = existing_order
        new_quantity = existing_quantity + quantity
        total = price * new_quantity
        cursor.execute(
            "UPDATE orders SET quantity = ?, total = ? WHERE orderid = ?",
            (new_quantity, total, orderid),
        )
        conn.commit()
        return orderid

    total = price * quantity
    cursor.execute(
        "INSERT INTO orders (menuid, quantity, total) VALUES (?, ?, ?)",
        (menuid, quantity, total),
    )
    conn.commit()
    return cursor.lastrowid
