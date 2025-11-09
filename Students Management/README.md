# 🎓 Student Management System (Flask + MySQL)

A simple **Flask web application** to manage student records — including adding, viewing, and deleting student information — with a MySQL database backend.

---

## 📁 Project Structure

```
│
├── app.py                # Main Flask application
├── studentdb.sql         # SQL script to create database and table
├── templates/
│   ├── index.html        # Homepage - lists all students
│   └── add_student.html  # Page for adding new students
├── README.md             # Project documentation
└── Requirement.txt       # Required tools 
```

> 📝 Note: Keep your `.html` files inside a folder named `templates` — Flask automatically searches for them there.

---

## ⚙️ Requirements

### 1️⃣ Software
- Python 3.x  
- MySQL Server  
- Any code editor (VS Code, PyCharm, etc.)

### 2️⃣ Python Libraries
Install dependencies using:
```bash
pip install flask mysql-connector-python
```

---

## 🗃️ Database Setup

1. Open MySQL and run the following commands:
   ```sql
   SOURCE studentdb.sql;
   ```
   This will:
   - Create a database `studentdb`
   - Create a table `students`
   - Add a `roll_no` column to store student roll numbers

2. You can verify:
   ```sql
   USE studentdb;
   SELECT * FROM students;
   ```

---

## 🚀 Running the Project

1. Start MySQL and ensure your credentials in `app.py` are correct:
   ```python
   conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="YourPassword",
       database="studentdb"
   )
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🌐 Features

✅ View all student records  
✅ Add new student (Name, Age, Roll Number, Branch)  
✅ Delete any student record  
✅ Simple and responsive HTML interface  

---

## 🧩 Future Enhancements
- Update/Edit student records  
- Search and filter students by branch or roll number  
- Authentication for admin login  
- Use Flask Blueprints for modular structure  

---

## 👨‍💻 Author
**Mohammad Iliyaz Mohammad Gari**  
📧 [mgiliyas8078@gmail.com](mailto:mgiliyas8078@gmail.com)
