from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import get_db, close_db
from order import add_order

app = Flask(__name__)
app.teardown_appcontext(close_db)

# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")

# MENU PAGE
@app.route("/menu")
def menu():
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

# ABOUT US PAGE
@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

# CHECKOUT PAGE
@app.route("/checkout")
def checkout():
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

if __name__ == "__main__":
    app.run(debug=True)