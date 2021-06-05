from flask import Flask, render_template, json, request, redirect, url_for
import os
import database.db_connector as db

app = Flask(__name__)
db_connection = db.connect_to_database()


@app.route('/')
def root():
        return render_template("main.j2")


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
                # Get Supplier names for display
                query = "SELECT Supplier_id, Supplier_name FROM Suppliers;"
                cursor = db.execute_query(db_connection, query)
                supplier_data = cursor.fetchall()
                supplier_names = {supplier['Supplier_id']:supplier['Supplier_name'] for supplier in supplier_data}
                cursor.close()
                return render_template("products.j2", products=results, supplier_names=supplier_names)
        if request.method == "POST":
                search_term = "%" + request.form['psearch'] +"%"
                query = 'SELECT * FROM Products WHERE Product_name LIKE %s'
                data = (search_term,)
                cursor = db.execute_query(db_connection, query, data)
                results = cursor.fetchall()
                print('Searching Products table for {}'.format(search_term))
                # Get Supplier names for display
                query = "SELECT Supplier_id, Supplier_name FROM Suppliers;"
                cursor = db.execute_query(db_connection, query)
                supplier_data = cursor.fetchall()
                supplier_names = {supplier['Supplier_id']:supplier['Supplier_name'] for supplier in supplier_data}
                cursor.close()
                return render_template("products.j2", products=results, supplier_names=supplier_names)


@app.route('/add_product', methods=["GET","POST"])
def add_product():
        if request.method == "GET":
                # Get Supplier names for display
                query = "SELECT Supplier_id, Supplier_name FROM Suppliers;"
                cursor = db.execute_query(db_connection, query)
                supplier_data = cursor.fetchall()
                supplier_names = [(supplier['Supplier_id'], supplier['Supplier_name']) for supplier in supplier_data]
                cursor.close()
                return render_template("add_product.j2", supplier_names=supplier_names)

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


@app.route('/delete_product/<int:id>')
def delete_product(id):
        query = 'DELETE FROM Products WHERE Product_id = %s'
        data = (id,)
        result = db.execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row deleted")
        return redirect(url_for('products'))


@app.route('/customers', methods=["GET","POST"])
def customers():
        if request.method == "GET":
                query = "SELECT * FROM Customers;"
                cursor = db.execute_query(db_connection=db_connection, query=query)
                results = cursor.fetchall()
                cursor.close()
                return render_template("customers.j2", customers=results)


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


@app.route('/update_customer/<int:id>', methods=["GET","POST"])
def update_customer(id):
        if request.method == "GET":
                customer_query = 'SELECT Customer_id, Customer_name, Customer_phone FROM Customers WHERE Customer_id = %s' % (id)
                customer_result = db.execute_query(db_connection, customer_query).fetchone()
                if not customer_result:
                        return "No such Customer"
                else:
                        return render_template('customer_update.j2', customer=customer_result)
        elif request.method == "POST":
                print('The POST request')
                customer_id = request.form['cid']
                customer_name = request.form['cname']
                customer_phone = request.form['cphone']
                query = 'UPDATE Customers SET Customer_name = %s, Customer_phone = %s WHERE Customer_id = %s'
                data = (customer_name, customer_phone, customer_id)
                result = db.execute_query(db_connection, query, data)
                print(str(result.rowcount) + " row(s) updated")
                return redirect(url_for('customers'))


@app.route('/orders', methods=["GET","POST"])
def orders():
        if request.method == "GET":
                query = "SELECT * FROM Orders;"
                cursor = db.execute_query(db_connection=db_connection, query=query)
                results = cursor.fetchall()
                # Get Customer names for display
                query = "SELECT Customer_id, Customer_name FROM Customers;"
                cursor = db.execute_query(db_connection, query)
                customer_data = cursor.fetchall()
                customer_names = {customer['Customer_id']:customer['Customer_name'] for customer in customer_data}
                cursor.close()
                return render_template("orders.j2", orders=results, customer_names=customer_names)


@app.route('/add_order', methods=["GET","POST"])
def add_order():
        if request.method == "GET":
                # Get Customer names for display
                query = "SELECT Customer_id, Customer_name FROM Customers;"
                cursor = db.execute_query(db_connection, query)
                customer_data = cursor.fetchall()
                customer_names = [(customer['Customer_id'], customer['Customer_name']) for customer in customer_data]
                cursor.close()
                return render_template("add_order.j2", customer_names=customer_names)

        if request.method == "POST":
                ord_cid = request.form['ord_cid']
                ord_date = request.form['ord_date']
                query = 'INSERT INTO Orders (Customer_id, Order_date) VALUES (%s,%s)'
                data = (ord_cid, ord_date)
                cursor = db.execute_query(db_connection, query, data)
                print('Added Order')
                cursor.close()
                return redirect(url_for('orders'))


@app.route('/order_products', methods=["GET"])
def order_products():
        if request.method == "GET":
                query = 'SELECT * FROM Order_products;'
                cursor = db.execute_query(db_connection, query)
                results = cursor.fetchall()
                # Get Product names for display
                query = "SELECT Product_id, Product_name FROM Products;"
                cursor = db.execute_query(db_connection, query)
                product_data = cursor.fetchall()
                product_names = {product['Product_id']:product['Product_name'] for product in product_data}
                cursor.close()
                return render_template("order_products.j2", order_products=results, product_names=product_names)


@app.route('/add_order_product', methods=["GET","POST"])
def add_order_product():
        if request.method == "GET":
                # Get Order IDs for display
                query = "SELECT Order_id FROM Orders;"
                cursor = db.execute_query(db_connection, query)
                order_data = cursor.fetchall()
                order_ids = [order['Order_id'] for order in order_data]
                order_ids.sort()
                # Get Product names for display
                query = "SELECT Product_id, Product_name FROM Products;"
                cursor = db.execute_query(db_connection, query)
                product_data = cursor.fetchall()
                product_names = [(product['Product_id'], product['Product_name']) for product in product_data]
                cursor.close()
                return render_template("add_order_product.j2", order_ids=order_ids, product_names=product_names)

        if request.method == "POST":
                ord_id = request.form['ord_id']
                prod_id = request.form['prod_id']
                quantity = request.form['quan']
                query = 'INSERT INTO Order_products (Order_id, Product_id, Quantity) VALUES (%s,%s,%s)'
                data = (ord_id, prod_id, quantity)
                cursor = db.execute_query(db_connection, query, data)
                print('Added Order Product')
                cursor.close()
                return redirect(url_for('order_products'))


@app.route('/purchase_products', methods=["GET","POST"])
def purchase_products():
        if request.method == "GET":
                query = 'SELECT * FROM Purchase_products;'
                cursor = db.execute_query(db_connection, query)
                results = cursor.fetchall()
                # Get Product names for display
                query = "SELECT Product_id, Product_name FROM Products;"
                cursor = db.execute_query(db_connection, query)
                product_data = cursor.fetchall()
                product_names = {product['Product_id']:product['Product_name'] for product in product_data}
                cursor.close()
                return render_template("purchase_products.j2", purchase_products=results, product_names=product_names)


@app.route('/add_purchase_product', methods=["GET","POST"])
def add_purchase_product():
        if request.method == "GET":
                # Get Purchase IDs for display
                query = "SELECT Purchase_id, Supplier_id FROM Purchases;"
                cursor = db.execute_query(db_connection, query)
                purchase_data = cursor.fetchall()
                purchase_ids = [purchase['Purchase_id'] for purchase in purchase_data]
                purchase_ids.sort()
                # Get Product names for display
                query = "SELECT Product_id, Product_name, Supplier_id FROM Products;"
                cursor = db.execute_query(db_connection, query)
                product_data = cursor.fetchall()
                product_names = [(product['Product_id'], product['Product_name'], product['Supplier_id']) for product in product_data]
                cursor.close()
                return render_template("add_purchase_product.j2", purchase_ids=purchase_ids, product_names=product_names)

        if request.method == "POST":
                pur_id = request.form['pur_id']
                prod_id = request.form['prod_id']
                quantity = request.form['quan']
                query = 'INSERT INTO Purchase_products (Purchase_id, Product_id, Quantity) VALUES (%s,%s,%s)'
                data = (pur_id, prod_id, quantity)
                cursor = db.execute_query(db_connection, query, data)
                print('Added Purchase Product')
                cursor.close()
                return redirect(url_for('purchase_products'))


@app.route('/suppliers', methods=["GET","POST"])
def suppliers():
        if request.method == "GET":
                query = "SELECT * FROM Suppliers;"
                cursor = db.execute_query(db_connection=db_connection, query=query)
                results = cursor.fetchall()
                cursor.close()
                return render_template("suppliers.j2", suppliers=results)


@app.route('/add_supplier', methods=["GET","POST"])
def add_supplier():
        if request.method == "POST":
                sname = request.form['sname']
                sloc = request.form['sloc']
                sphone = request.form['sphone']
                query = 'INSERT INTO Suppliers (Supplier_name, Supplier_location, Supplier_phone) VALUES (%s,%s,%s)'
                data = (sname, sloc, sphone)
                cursor = db.execute_query(db_connection, query, data)
                print('Added Supplier: {}'.format(sname))
                cursor.close()
                return redirect(url_for('suppliers'))
        return render_template('add_supplier.j2')


@app.route('/purchases', methods=["GET","POST"])
def purchases():
        if request.method == "GET":
                query = "SELECT * FROM Purchases;"
                cursor = db.execute_query(db_connection=db_connection, query=query)
                results = cursor.fetchall()
                # Get Supplier names for display
                query = "SELECT Supplier_id, Supplier_name FROM Suppliers;"
                cursor = db.execute_query(db_connection, query)
                supplier_data = cursor.fetchall()
                supplier_names = {supplier['Supplier_id']:supplier['Supplier_name'] for supplier in supplier_data}
                cursor.close()
                return render_template("purchases.j2", purchases=results, supplier_names=supplier_names)


@app.route('/add_purchase', methods=["GET","POST"])
def add_purchase():
        if request.method == "GET":
                # Get Supplier names for display
                query = "SELECT Supplier_id, Supplier_name FROM Suppliers;"
                cursor = db.execute_query(db_connection, query)
                supplier_data = cursor.fetchall()
                supplier_names = [(supplier['Supplier_id'], supplier['Supplier_name']) for supplier in supplier_data]
                cursor.close()
                return render_template("add_purchase.j2", supplier_names=supplier_names)

        if request.method == "POST":
                pur_sid = request.form['pur_sid']
                pur_date = request.form['pur_date']
                query = 'INSERT INTO Purchases (Supplier_id, Purchase_date) VALUES (%s,%s)'
                data = (pur_sid, pur_date)
                cursor = db.execute_query(db_connection, query, data)
                print('Added Purchase')
                cursor.close()
                return redirect(url_for('purchases'))


if __name__=="__main__":
        port = int(os.environ.get('PORT', 52935))
        app.run(port=port, debug=False)
