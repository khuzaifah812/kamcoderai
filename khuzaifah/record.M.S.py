import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT,
    age INTEGER
)
""")
conn.commit()


def add_student():
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    age = int(input("Enter Age: "))

    cursor.execute(
        "INSERT INTO students(name,course,age) VALUES(?,?,?)",
        (name, course, age)
    )

    conn.commit()
    print("Student Added Successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n--- STUDENT RECORDS ---")
    for row in records:
        print(f"ID:{row[0]} Name:{row[1]} Course:{row[2]} Age:{row[3]}")


def search_student():
    name = input("Enter student name: ")

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    results = cursor.fetchall()

    if results:
        for row in results:
            print(f"ID:{row[0]} Name:{row[1]} Course:{row[2]} Age:{row[3]}")
    else:
        print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID: ")

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    print("Student Deleted Successfully")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        conn.close()
        print("Goodbye!")
        break

    else:
        print("Invalid choice")