from flask import Flask, render_template, json, request, redirect, url_for
import os
import database.db_connector as db

app = Flask(__name__)
db_connection = db.connect_to_database()

#Sample data
order_products_headers = ("Order_ID", "Product_ID", "Quantity")
order_products_data = [[1, 2, 3],
                        [1, 4, 1],
                        [2, 1, 10]]

purchase_products_headers = ("Purchase_ID", "Product_ID", "Quantity")
purchase_products_data = [[1, 2, 5],
                        [1, 3, 10],
                        [2, 1, 15]]

purchases_headers = ("Purchase_ID", "Supplier_ID", "Purchase_date")
purchases_data = [[1, 1, "2021-04-21"],
                [2, 1, "2021-04-10"]]


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
                cursor.close()
                return render_template("products.j2", products=results)
        if request.method == "POST":
                search_term = "%" + request.form['psearch'] +"%"
                query = 'SELECT * FROM Products WHERE Product_name LIKE %s'
                data = (search_term,)
                cursor = db.execute_query(db_connection, query, data)
                results = cursor.fetchall()
                print('Searching Products table for {}'.format(search_term))
                cursor.close()
                return render_template("products.j2", products=results)

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
                cursor.close()
                return render_template("orders.j2", orders=results)

@app.route('/add_order', methods=["GET","POST"])
def add_order():
        if request.method == "POST":
                ord_cid = request.form['ord_cid']
                ord_date = request.form['ord_date']
                query = 'INSERT INTO Orders (Customer_id, Order_date) VALUES (%s,%s)'
                data = (ord_cid, ord_date)
                cursor = db.execute_query(db_connection, query, data)
                print('Added Order')
                cursor.close()
                return redirect(url_for('orders'))
        return render_template('add_order.j2')


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
                cursor.close()
                return render_template("purchases.j2", purchases=results)

@app.route('/add_purchase', methods=["GET","POST"])
def add_purchase():
        if request.method == "POST":
                pur_sid = request.form['pur_sid']
                pur_date = request.form['pur_date']
                query = 'INSERT INTO Purchases (Supplier_id, Purchase_date) VALUES (%s,%s)'
                data = (pur_sid, pur_date)
                cursor = db.execute_query(db_connection, query, data)
                print('Added Purchase')
                cursor.close()
                return redirect(url_for('purchases'))
        return render_template('add_purchase.j2')


if __name__=="__main__":
        port = int(os.environ.get('PORT', 52935))
        app.run(port=port, debug=False)