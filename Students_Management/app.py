from flask import Flask, render_template, request, redirect, session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"

# DB connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iliyas@486",
    database="studentdb"
)
cursor = conn.cursor(dictionary=True)

# ---------- REGISTER ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check user exists
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        if cursor.fetchone():
            return "User already exists"

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        conn.commit()

        return redirect('/login')

    return render_template('register.html')

#-------      LOGIN      -----
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cursor.fetchone()

        if user:
            session['user'] = username
            return redirect('/')
        else:
            return "Invalid Credentials"

    return render_template('login.html')
@app.route('/logout')
def logout():
    if 'user' not in session:
        return redirect('/login')
    session.pop('user', None)   # remove logged-in user
    return redirect('/login')

# ---------- HOME + SEARCH ----------
@app.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')

    search = request.args.get('search')

    if search:
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE %s OR roll_no LIKE %s",
            ('%' + search + '%', '%' + search + '%')
        )
    else:
        cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()
    return render_template('index.html', students=students)

# ---------- ADD ----------
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        roll_no = request.form['roll_no']
        branch = request.form['branch']

        # Validation
        if not name or not age.isdigit():
            return "Invalid Data"

        # Unique roll_no check
        cursor.execute("SELECT * FROM students WHERE roll_no=%s", (roll_no,))
        if cursor.fetchone():
            return "Roll Number Already Exists"

        cursor.execute(
            "INSERT INTO students (name, age, roll_no, branch) VALUES (%s,%s,%s,%s)",
            (name, age, roll_no, branch)
        )
        conn.commit()

        return redirect('/')

    return render_template('add_student.html')

# ---------- UPDATE ----------
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        roll_no = request.form['roll_no']
        branch = request.form['branch']

        cursor.execute("""
            UPDATE students
            SET name=%s, age=%s, roll_no=%s, branch=%s
            WHERE id=%s
        """, (name, age, roll_no, branch, id))
        conn.commit()

        return redirect('/')

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    return render_template('update_student.html', student=student)

# ---------- DELETE ----------
@app.route('/delete/<int:id>')
def delete_student(id):
    if 'user' not in session:
        return redirect('/login')

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    return redirect('/')

# ---------- API ----------
@app.route('/api/students')
def api_students():
    if 'user' not in session:
        return redirect('/login')
    cursor.execute("SELECT * FROM students")
    return jsonify(cursor.fetchall())

# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)