from flask import Flask, render_template, json, request, redirect, url_for
import os
import database.db_connector as db

app = Flask(__name__)
db_connection = db.connect_to_database()

#Sample data
products_headers = ("Item_ID", "Name", "Supplier_ID", "Unit_cost", "Unit_price", "Quantity")
products_data = [[1, "CCBC Tropicalia", 1, 10, 8, 100],
        [2, "CCBC Bibo", 1, 9, 7, 100],
        [3, "CCBC Silent World", 1, 10, 8, 50],
        [4, "Allagash White", 2, 10, 8, 50],
        [5, "Saison Dupont", 3, 12, 9, 25]]    

customers_headers = ("Customer_ID", "Customer_name", "Customer_phone")
customers_data = [[1, "Steve", "555-555-5555"],
                [2, "John B", "444-444-4444"],
                [3, "Steve 2", "333-333-3333"]]

orders_headers = ("Order_ID", "Customer_ID", "Order_date")
orders_data = [[1, 1, "2021-04-01"],
                [2, 1, "2021-03-25"]]

order_products_headers = ("Order_ID", "Product_ID", "Quantity")
order_products_data = [[1, 2, 3],
                        [1, 4, 1],
                        [2, 1, 10]]

purchase_products_headers = ("Purchase_ID", "Product_ID", "Quantity")
purchase_products_data = [[1, 2, 5],
                        [1, 3, 10],
                        [2, 1, 15]]

suppliers_headers = ("Supplier_ID", "Supplier_name", "Supplier_location", "Supplier_phone")
suppliers_data = [[1, "Creature Comforts Brewing", "Athens, GA", "555-555-5551"],
                [2, "Allagash Brewing", "Portland, ME", "111-111-1111"],
                [3, "Brasserie Dupont", "Belgium", "222-222-2222"]]

purchases_headers = ("Purchase_ID", "Supplier_ID", "Purchase_date")
purchases_data = [[1, 1, "2021-04-21"],
                [2, 1, "2021-04-10"]]


@app.route('/')
def root():
        return render_template("main.j2", my_string="Test string", my_list=[0,1,2,3,4,5])

@app.route('/index')
def index():
        return render_template("index.j2")

@app.route('/db-test')
def db_test():
    query = "SELECT * FROM bsg_people;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    print(results)
    return render_template("db_test.j2", bsg_people=results)

@app.route('/products', methods=["GET","POST"])
def products():
        if request.method == "GET":
                query = "SELECT * FROM Products;"
                cursor = db.execute_query(db_connection=db_connection, query=query)
                results = cursor.fetchall()
                cursor.close()
                return render_template("products.j2", products=results)
        # if request.method == "POST":
        #         product_name = request.form['pname']
        #         product_supplierID = request.form['p_sid']
        #         product_cost = request.form['p_cost']
        #         product_price = request.form['p_price']
        #         product_quantity = request.form['p_quan']
        #         products_data.append([len(products_data)+1, product_name, product_supplierID, product_cost, product_price, product_quantity])

        return render_template("products.j2", headers=products_headers, rows=products_data)

@app.route('/add_product', methods=["GET","POST"])
def add_product():
        if request.method == "POST":
                pname = request.form['pname']
                p_sid = request.form['p_sid']
                p_cost = request.form['p_cost']
                p_price = request.form['p_price']
                p_quan = request.form['p_quan']
                query = 'INSERT INTO Products (Product_name, Supplier_id, Unit_cost, Unit_price, Quantity) VALUES (%s,%s,%s,%s,%s)'
                data = (pname,p_sid,p_cost,p_price,p_quan)
                cursor = db.execute_query(db_connection, query, data)
                print('Added product')
                cursor.close()
                return redirect(url_for('products'))
        return render_template('add_product.j2')

@app.route('/customers', methods=["GET","POST"])
def customers():
        if request.method == "GET":
                query = "SELECT * FROM Customers;"
                cursor = db.execute_query(db_connection=db_connection, query=query)
                results = cursor.fetchall()
                cursor.close()
                return render_template("customers.j2", customers=results)
        # if request.method == "POST":
        #         cname = request.form['cname']
        #         cphone = request.form['cphone']
        #         customers_data.append([len(customers_data)+1, cname, cphone])
        return render_template("customers.j2", headers=customers_headers, rows=customers_data)

@app.route('/add_customer', methods=["GET","POST"])
def add_customer():
        if request.method == "POST":
                cname = request.form['cname']
                cphone = request.form['cphone']
                query = 'INSERT INTO Customers (Customer_name, Customer_phone) VALUES (%s,%s)'
                data = (cname, cphone)
                cursor = db.execute_query(db_connection, query, data)
                print('Added Customer')
                cursor.close()
                return redirect(url_for('customers'))
        return render_template('add_customer.j2')

@app.route('/orders', methods=["GET","POST"])
def orders():
        if request.method == "POST":
                order_customerID = request.form['ord_cid']
                order_date = request.form['ord_date']
                orders_data.append([len(orders_data)+1, order_customerID, order_date])

        return render_template("orders.j2", headers=orders_headers, rows=orders_data)

@app.route('/order_products', methods=["GET","POST","DELETE"])
def order_products():
        if request.method == "POST":
                order_products_orderID = request.form['ord_prod_ord_id']
                order_products_productID = request.form['ord_prod_prod_id']
                order_products_quan = request.form['ord_prod_quan']
                order_products_data.append([order_products_orderID, order_products_productID, order_products_quan])
        elif request.method == "DELETE":
                print(request.args)
                print("test")

        return render_template("order_products.j2", headers=order_products_headers, rows=order_products_data)

@app.route('/purchase_products', methods=["GET","POST"])
def purchase_products():
        if request.method == "POST":
                purchase_products_purchaseID = request.form['pur_prod_pur_id']
                purchase_products_productID = request.form['pur_prod_prod_id']
                purchase_products_quan = request.form['pur_prod_quan']
                purchase_products_data.append([purchase_products_purchaseID, purchase_products_productID, purchase_products_quan])

        return render_template("purchase_products.j2", headers=purchase_products_headers, rows=purchase_products_data)

@app.route('/suppliers', methods=["GET","POST"])
def suppliers():
        if request.method == "POST":
                sname = request.form['sname']
                sloc = request.form['sloc']
                sphone = request.form['sphone']
                suppliers_data.append([len(suppliers_data)+1, sname, sloc, sphone])

        return render_template("suppliers.j2", headers=suppliers_headers, rows=suppliers_data)

@app.route('/purchases', methods=["GET","POST"])
def purchases():
        if request.method == "POST":
                purchase_supplierID = request.form['pur_sid']
                purchase_date = request.form['pur_date']
                purchases_data.append([len(purchases_data)+1, purchase_supplierID, purchase_date])

        return render_template("purchases.j2", headers=purchases_headers, rows=purchases_data)

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