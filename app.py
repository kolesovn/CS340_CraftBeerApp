from flask import Flask, render_template, json, request
import os
#import database.db_connector as db

app = Flask(__name__)
#db_connection = db.connect_to_database()


@app.route('/')
def root():
        return render_template("main.j2", my_string="Test string", my_list=[0,1,2,3,4,5])

@app.route('/index')
def index():
        return render_template("index.j2")

@app.route('/products')
def products():
        headers = ("Item_ID", "Name", "Supplier_ID", "Unit_cost", "Unit_price", "Quantity")
        data = [[1, "CCBC Tropicalia", 1, 10, 8, 100],
                [2, "CCBC Bibo", 1, 9, 7, 100],
                [3, "CCBC Silent World", 1, 10, 8, 50],
                [4, "Allagash White", 2, 10, 8, 50],
                [5, "Saison Dupont", 3, 12, 9, 25]]       
        return render_template("products.j2", headers=headers, rows=data)

@app.route('/customers', methods=["GET","POST"])
def customers():
        headers = ("Customer_ID", "Customer_name", "Customer_phone")
        rows = [[1, "Steve", "555-555-5555"],
                [2, "John B", "444-444-4444"],
                [3, "Steve 2", "333-333-3333"]]

        if request.method == "POST":
                cname = request.form['cname']
                cphone = request.form['cphone']
                rows.append([len(rows)+1, cname, cphone])
                print(rows)

        return render_template("customers.j2", headers=headers, rows=rows)

@app.route('/orders')
def orders():
        headers = ("Order_ID", "Customer_ID", "Order_date")
        rows = [[1, 1, "2021-04-01"],
                [2, 1, "2021-03-25"]]
        return render_template("orders.j2", headers=headers, rows=rows)

@app.route('/order_products')
def order_products():
        headers = ("Order_ID", "Product_ID", "Quantity")
        rows = [[1, 2, 3],
                [1, 4, 1],
                [2, 1, 10]]
        return render_template("order_products.j2", headers=headers, rows=rows)

@app.route('/purchase_products')
def purchase_products():
        headers = ("Purchase_ID", "Product_ID", "Quantity")
        rows = [[1, 2, 5],
                [1, 3, 10],
                [2, 1, 15]]
        return render_template("purchase_products.j2", headers=headers, rows=rows)

@app.route('/suppliers')
def suppliers():
        headers = ("Supplier_ID", "Supplier_name", "Supplier_location", "Supplier_phone")
        rows = [[1, "Creature Comforts Brewing", "Athens, GA", "555-555-5551"],
                [2, "Allagash Brewing", "Portland, ME", "111-111-1111"],
                [3, "Brasserie Dupont", "Belgium", "222-222-2222"]]
        return render_template("suppliers.j2", headers=headers, rows=rows)

@app.route('/purchases')
def purchases():
        headers = ("Purchase_ID", "Supplier_ID", "Purchase_date")
        rows = [[1, 1, "2021-04-21"],
                [2, 1, "2021-04-10"]]
        return render_template("purchases.j2", headers=headers, rows=rows)

@app.route('/view_inventory')
def view_inventory():
        return render_template("view_inventory.j2")

@app.route('/view_product_admin')
def view_prduct_admin():
        return render_template("view_prduct_admin.j2")

@app.route('/view_product_customer')
def view_product_customer():
        return render_template("view_product_customer.j2")

@app.route('/view_cart')
def view_cart():
        return render_template("view_cart.j2")


if __name__=="__main__":
        port = int(os.environ.get('PORT', 52935))
        app.run(port=port, debug=False)