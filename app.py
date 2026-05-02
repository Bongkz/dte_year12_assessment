from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")

# MENU PAGE
@app.route("/menu")
def menu():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Menu")
    items = cursor.fetchall()

    conn.close()

    return render_template("menu.html", items=items)

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