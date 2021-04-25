from flask import Flask, render_template, json
import os
import database.db_connector as db

app = Flask(__name__)
db_connection = db.connect_to_database()

@app.route('/')
def root():
        return render_template("main.j2")

@app.route('/bsg-people')
def bsg_people():
        query = "SELECT * FROM bsg_db.sql"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template("bsg.j2", bsg_people=results)

@app.route('/task1')
def task1():
        query = "SELECT * FROM task1"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("task1.j2", results=results)


if __name__=="__main__":
        port = int(os.environ.get('PORT', 52935))
        app.run(port=port, debug=False)