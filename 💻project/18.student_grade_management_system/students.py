import json
import os

# JSON file to store student data
DATA_FILE = "students_data.json"

# Load existing data from JSON file if it exists
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Save data to JSON file
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(student_grades, file)

# Dictionary to hold student data
student_grades = load_data()

def add_student(name, grade):
    student_grades[name] = grade
    save_data()
    print(f"Student {name} added with grade {grade}.")

def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        save_data()
        print(f"Grade for student {name} updated to {grade}.")
    else:
        print(f"Student {name} not found.")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        save_data()
        print(f"Student {name} has been deleted.")
    else:
        print(f"Student {name} not found.")

def display_all_students():
    if student_grades:
        print("\nStudent Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")

def main():
    while True:
        print("\nStudent Grades Management System")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice = ")

        if choice == "1":
            name = input("Enter student name = ")
            try:
                grade = int(input("Enter student grade = "))
                add_student(name, grade)
            except ValueError:
                print("Invalid input. Please enter a valid number for the grade.")

        elif choice == "2":
            name = input("Enter student name = ")
            try:
                grade = int(input("Enter new grade = "))
                update_grade(name, grade)
            except ValueError:
                print("Invalid input. Please enter a valid number for the grade.")

        elif choice == "3":
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == "4":
            display_all_students()

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the program
main()
