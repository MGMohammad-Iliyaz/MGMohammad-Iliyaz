from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# Database connection using environment variables
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST", "mydb-abcd1234.render.com"),  # replace default with your actual host
    user=os.getenv("DB_USER", "render"),
    password=os.getenv("DB_PASS", "Iliyas@486"),
    database=os.getenv("DB_NAME", "studentdb"),
    port=int(os.getenv("DB_PORT", 3306))
)

cursor = connection.cursor(dictionary=True)

# Home page - view all students
@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)

# Add student page
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        roll_no = request.form['roll_no']
        branch = request.form['branch']

        sql = "INSERT INTO students (name, age, roll_no, branch) VALUES (%s, %s, %s, %s)"
        data = (name, age, roll_no, branch)
        cursor.execute(sql, data)
        connection.commit()
        return redirect('/')
    return render_template('add_student.html')

# Delete student
@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    connection.commit()
    return redirect('/')

if __name__ == '__main__':
    # For deployment on Render, bind to 0.0.0.0
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
