# main.py
# Console user interface

from student_manager import StudentManager
from database import create_table

def main():
    create_table()
    manager = StudentManager()

    while True:
        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                name = input("Enter student name: ").strip()
                age = int(input("Enter student age: "))
                marks = float(input("Enter student marks: "))
                manager.add_student(name, age, marks)

            elif choice == "2":
                manager.display_all_students()

            elif choice == "3":
                student_id = int(input("Enter student ID to search: "))
                manager.search_student(student_id)

            elif choice == "4":
                student_id = int(input("Enter student ID to update: "))
                name = input("Enter new name: ").strip()
                age = int(input("Enter new age: "))
                marks = float(input("Enter new marks: "))
                manager.update_student(student_id, name, age, marks)

            elif choice == "5":
                student_id = int(input("Enter student ID to delete: "))
                manager.delete_student(student_id)

            elif choice == "6":
                print("\nThank you for using Student Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input! Please enter correct numbers.")

if __name__ == "__main__":
    main()