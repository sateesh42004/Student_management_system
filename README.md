# Student Management System

A simple command-line based Student Management System built using Python. This project allows users to manage student records efficiently using CRUD operations (Create, Read, Update, Delete).

## Features

* Add a new student
* View all student records
* Update student details
* Delete a student record
* Prevent duplicate Student IDs
* Store multiple student attributes:

  * Student ID
  * Name
  * Marks
  * Age
  * Weight

## Technologies Used

* Python 3
* Dictionaries
* Functions
* Loops
* Conditional Statements

## Project Structure

Each student record is stored using a nested dictionary:

```python
students = {
    101: {
        "name": "John",
        "marks": 95,
        "age": 20,
        "weight": 65.5
    }
}
```

## Menu Options

1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

## How to Run

### Clone the Repository

```bash
git clone https://github.com/https://github.com/sateesh42004/Student_management_system.git
```

### Navigate to the Project Folder

```bash
cd Student_management_system
```

### Run the Program

```bash
python main.py
```

## Example Output

```text
===== Student Management System =====

1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Enter your choice:
```

## Learning Outcomes

This project helped practice:

* Python fundamentals
* Functions
* Dictionaries and Nested Dictionaries
* CRUD Operations
* User Input Handling
* Menu-Driven Programs

## Future Improvements

* Search Student by ID
* Search Student by Name
* Calculate Average Marks
* Display Top Scorer
* Save Data to JSON File
* Load Data from JSON File
* Sort Students by Marks
* Graphical User Interface (GUI)

## Author

Sateesh

## License

This project is open-source and available for learning and educational purposes.
