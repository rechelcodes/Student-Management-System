FILE_NAME = "students.txt"

students = []

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, id, department, degree = line.split(",")
                    students.append({"name": name, "id": id, "department": department, "degree": degree})
            print("\nStudent data loaded successfully!")
    except FileNotFoundError:
        print("\nNo existing student data found. Starting fresh.")

def save_students():
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['id']},{student['department']},{student['degree']}\n")
    print("\nStudent data saved successfully!")

def add_student():
    name = input("Enter student name: ")
    id = input("Enter student ID: ")
    department = input("Enter student department: ")
    degree = input("Enter student degree: ")
    student = {"name": name, "id": id, "department": department, "degree": degree}
    students.append(student)
    save_students()
    print("\nStudent added successfully!")

def view_all_student():
    if not students:
        print("\nNo students to display.")
    else:
        print("\n" + "-" * 30)
        print(f"{'Student List':^30}")
        print("=" * 30)
        for index, student in enumerate(students, start=1):
            print(f"\nStudent {index}")
            print("-" * 30)
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Department: {student['department']}")
            print(f"Degree: {student['degree']}")
            print("-" * 30)

def search_student():
    roll = input("\nEnter the ID you want to search: ")
    found = [student for student in students if student["id"] == roll]
    if found:
        print("\nStudent found!")
        print("-" * 30)
        for student in found:
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Department: {student['department']}")
            print(f"Degree: {student['degree']}")
            print("-" * 30)
    else:
        print("\nStudent not found.")

def edit_student():
    id = input("Enter the student ID you want to edit: ")
    for student in students:
        if student["id"] == id:
            new_name = input("Enter New Name: ")
            new_department = input("Enter New Department: ")
            new_degree = input("Enter New Degree: ")
            new_id = input("Enter New ID: ")
            student.update({"name": new_name, "id": new_id, "department": new_department, "degree": new_degree})
            save_students()
            print("\nStudent profile updated successfully!")
            return
    print("\nStudent not found.")

def delete_student():
    id = input("Enter the student ID you want to delete: ")
    for student in students:
        if student["id"] == id:
            students.remove(student)
            save_students()
            print("\nStudent has been removed.")
            return
    print("\nStudent not found.")

load_students()
while True:
    print("\n" + "=" * 40)
    print(f"{'Student Management System':^40}")
    print("=" * 40)
    print("\nProject Menu")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by ID")
    print("4. Edit Student Profile")
    print("5. Delete Profile")
    print("6. EXIT")
    print("=" * 40)
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        edit_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Try again.")
        