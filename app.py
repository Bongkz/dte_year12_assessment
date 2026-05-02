from flask import Flask, render_template, request, redirect, url_for
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
        return redirect(url_for("menu"))

    add_order(menuid, quantity)
    return redirect(url_for("checkout"))

# ABOUT US PAGE
@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

# CHECKOUT PAGE
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(debug=True)