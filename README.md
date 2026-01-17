# 🎓 Student Registration System (Python + Tkinter + MySQL)

A **desktop-based Student Registration System** developed using **Python Tkinter** for the graphical user interface and **MySQL** for database management.  
This application supports full **CRUD operations** (Create, Read, Update, Delete) and displays records dynamically using a Treeview widget.

---

## 🚀 Features

- ➕ Add new student records  
- ✏️ Update existing student details  
- 🗑️ Delete student records  
- 📋 View all students in a Treeview table  
- 🖱️ Auto-fill input fields on record selection  
- ⚠️ Input validation and error handling  
- 🔐 Secure database operations using parameterized queries  

---

## 🛠️ Tech Stack

- **Python**
- **Tkinter** (GUI Development)
- **MySQL**
- **mysql-connector-python**
- **ttk Treeview**

---

## 🗄️ Database Structure

**Database Name:** `webgui`  
**Table Name:** `registration`

```sql
CREATE DATABASE webgui;

USE webgui;

CREATE TABLE registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    course VARCHAR(100),
    fee VARCHAR(50)
);
