# Student Management System

students = {}


def add_student():
    std_id = int(input("Enter student ID: "))

    if std_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    age = int(input("Enter student age: "))
    weight = float(input("Enter student weight: "))

    students[std_id] = {
        "name": name,
        "marks": marks,
        "age": age,
        "weight": weight
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found!")
        return

    for i, (std_id, info) in enumerate(students.items(), start=1):
        print(f"""
{i}. Student Details
-------------------
ID     : {std_id}
Name   : {info['name']}
Marks  : {info['marks']}
Age    : {info['age']}
Weight : {info['weight']}
""")


def update_student():
    std_id = int(input("Enter student ID to update: "))

    if std_id not in students:
        print("Student not found.")
        return

    change = input(
        "What do you want to update? (name/marks/age/weight): "
    ).lower()

    if change == "name":
        students[std_id]["name"] = input("Enter new name: ")

    elif change == "marks":
        students[std_id]["marks"] = int(input("Enter new marks: "))

    elif change == "age":
        students[std_id]["age"] = int(input("Enter new age: "))

    elif change == "weight":
        students[std_id]["weight"] = float(input("Enter new weight: "))

    else:
        print("Invalid field!")
        return

    print(f"Student ID {std_id} updated successfully!")


def delete_student():
    std_id = int(input("Enter student ID to delete: "))

    if std_id in students:
        del students[std_id]
        print(f"Student ID {std_id} deleted successfully!")
    else:
        print(f"Student ID {std_id} not found.")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting the Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")