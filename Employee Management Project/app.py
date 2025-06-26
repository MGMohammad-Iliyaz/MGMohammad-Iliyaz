from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'employee_db'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', employees=data)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO employees (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_employee(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employees WHERE id = %s", (id,))
    mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
