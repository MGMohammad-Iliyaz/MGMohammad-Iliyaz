# Student Management System

A full-stack web application built using Flask and MySQL to manage student records with authentication.

## 🚀 Features
- User Registration & Login
- Session-based Authentication
- Add, Update, Delete Students
- Search Functionality
- REST API Endpoint
- Clean UI with CSS

## 🛠️ Tech Stack
- Python (Flask)
- MySQL
- HTML, CSS

## 📁 Project Structure
student_management/
│
├── app.py
├── README.md
├── LICENSE
├── requirements.txt

│
├── static/
   ├──stle.css
├── templates/
   ├──add_student.html
   ├──index.html
   ├──login.html
   ├──register.html
   ├──update.html
├── database/
   ├──studentdb.sql


## ⚙️ Setup Instructions

1. Clone repository
2. Install dependencies:

pip install -r requirements.txt


3. Setup MySQL database:

Run database/schema.sql


4. Run application:

python app.py


5. Open browser:

http://127.0.0.1:5000/login


## 🔗 API Endpoint

GET /api/students


## 👨‍💻 Author
Mohammad Iliyaz