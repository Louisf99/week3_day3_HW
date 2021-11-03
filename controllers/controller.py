from flask import render_template
from app import app
from models.orders_list import orders

@app.route('/')
def Home():
    return 'Home'

@app.route('/orders')
def index():
    return render_template('index.html', title="Order list", orders=orders )


@app.route('/orders/<index>')
def order_index():
    return render_template('order.html', title="order", orders=orders[1])
    