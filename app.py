from flask import Flask, render_template, json
import os
import database.db_connector as db

app = Flask(__name__)
db_connection = db.connect_to_database()

@app.route('/index')
def root():
        return render_template("index.j2")

@app.route('/')
def root():
        return render_template("main.j2")

@app.route('/product_search')
def root():
        return render_template("product_search.j2")

@app.route('/view_product_customer')
def root():
        return render_template("view_product_customer.j2")

@app.route('/view_cart')
def root():
        return render_template("view_cart.j2")

@app.route('/supplier_search')
def root():
        return render_template("supplier_search.j2")

@app.route('/view_inventory')
def root():
        return render_template("view_inventory.j2")

@app.route('/view_prduct_admin')
def root():
        return render_template("view_prduct_admin.j2")

@app.route('/resupply_order')
def root():
        return render_template("resupply_order.j2")



if __name__=="__main__":
        port = int(os.environ.get('PORT', 52935))
        app.run(port=port, debug=False)