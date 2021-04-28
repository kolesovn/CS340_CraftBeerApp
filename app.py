from flask import Flask, render_template, json
import os
#import database.db_connector as db

app = Flask(__name__)
#db_connection = db.connect_to_database()

@app.route('/index')
def index():
        return render_template("index.j2")

@app.route('/')
def root():
        return render_template("main.j2", my_string="Test string", my_list=[0,1,2,3,4,5])

@app.route('/product_search')
def product_search():
        return render_template("product_search.j2")

@app.route('/view_product_customer')
def view_product_customer():
        return render_template("view_product_customer.j2")

@app.route('/view_cart')
def view_cart():
        return render_template("view_cart.j2")

@app.route('/supplier_search')
def supplier_search():
        return render_template("supplier_search.j2")

@app.route('/view_inventory')
def view_inventory():
        return render_template("view_inventory.j2")

@app.route('/view_product_admin')
def view_prduct_admin():
        return render_template("view_prduct_admin.j2")

@app.route('/resupply_order')
def resupply_order():
        return render_template("resupply_order.j2")



if __name__=="__main__":
        port = int(os.environ.get('PORT', 52935))
        app.run(port=port, debug=False)