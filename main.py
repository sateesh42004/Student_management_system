# Student Management System
students = {}
def add_student():
  name = input("enter student name: ")
  marks = int(input("enter student marks: "))
  students[name] = marks
  print("Student added successfully!")
def view_students():
  i = 1
  for name,marks in students.items():
    print(f"{i}. Name: {name}, Marks: {marks}")
    i += 1
def update_student():
  name = input("enter student name to update: ")
  if name in students:
    marks = int(input("enter new marks: "))
    students[name] = marks
    print("Student updated successfully!")
  else:
    print("Student not found.")
def delete_student():
  name = input("enter student name to delete: ")
  if name in students:
    del students[name]
    print(f"Student '{name}' deleted successfully!")
  else:
    print(f"Student '{name}' not found.")
  


while True:
  print("####Welcome to the Student Management System #### \n")
  print("1. Add Student\n")
  print("2. View Students\n")
  print("3. Update Student\n")
  print("4. Delete Student\n")
  print("5. Exit\n")
  choice = input("Enter your choice: ")
  if choice == '1':
    add_student()
  elif choice == '2':
    view_students()
  elif choice == '3':
    update_student()
  elif choice == '4':
    delete_student()
  elif choice == '5':
    print("Exiting the Student Management System. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")