from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import get_db, close_db
from order import add_order

app = Flask(__name__)
app.teardown_appcontext(close_db)

# Shows home page when user goes to "/"
@app.route("/")
def home_page():
    return render_template("index.html")

# Shows menu page when user goes to "/menu"
@app.route("/menu")
def menu_page():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Menu")
    items = cursor.fetchall()

    return render_template("menu.html", items=items)

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    menuid = request.form.get("menuid", type=int)
    quantity = request.form.get("quantity", type=int, default=1)

    if menuid is None or quantity < 1:
        if request.accept_mimetypes.accept_json:
            return jsonify({"success": False, "message": "Invalid item."}), 400
        return redirect(url_for("menu"))

    add_order(menuid, quantity)
    if request.accept_mimetypes.accept_json:
        return jsonify({"success": True, "message": "Item Added to Cart"})
    return redirect(url_for("checkout"))

# Shows about us page when user goes to "/aboutus"
@app.route("/aboutus")
def aboutus_page():
    return render_template("aboutus.html")

# Shows checkout page when user goes to "/checkout"
@app.route("/checkout")
def checkout_page():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT orders.orderid, menu.name, menu.price, orders.quantity, orders.total
        FROM orders
        JOIN menu ON orders.menuid = menu.menuid
        ORDER BY orders.order_time DESC
    """)
    cart_items = cursor.fetchall()

    total = sum(item[4] for item in cart_items)  # item[4] is total

    return render_template("checkout.html", cart_items=cart_items, total=total)

@app.route("/remove_item/<int:orderid>", methods=["POST"])
def remove_item(orderid):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM orders WHERE orderid = ?", (orderid,))
    conn.commit()

    return redirect(url_for("checkout"))

@app.route("/clear_cart", methods=["POST"])
def clear_cart():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM orders")
    conn.commit()

    return jsonify({"success": True, "message": "Cart cleared"})

if __name__ == "__main__":
    app.run(debug=True)