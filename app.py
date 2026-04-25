from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/checkout')
def checkout():
    # This grabs the "item" and "price" from the URL
    item_name = request.args.get('item', 'Nothing')
    item_price = request.args.get('price', '0.00')
    
    return render_template('checkout.html', item=item_name, price=item_price)

if __name__ == '__main__':
    app.run(debug=True)