class StudentManagementSystem:
    FILE_NAME = "students.txt"
    students = []

    def load_students(self):
        try:
            with open(StudentManagementSystem.FILE_NAME, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        name, id, department, degree = line.split(",")
                        StudentManagementSystem.students.append({"name": name, "id": id, "department": department, "degree": degree})
                print("\nStudent data loaded successfully!")
        except FileNotFoundError:
            print("\nNo existing student data found. Starting fresh.")

    def save_students(self):
        with open(StudentManagementSystem.FILE_NAME, "w") as file:
            for student in StudentManagementSystem.students:
                file.write(f"{student['name']},{student['id']},{student['department']},{student['degree']}\n")
        print("\nStudent data saved successfully!")

    def add_student(self):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        department = input("Enter student department: ")
        degree = input("Enter student degree: ")
        student = {"name": name, "id": id, "department": department, "degree": degree}
        StudentManagementSystem.students.append(student)
        self.save_students()
        print("\nStudent added successfully!")

    def view_all_students(self):
        if not StudentManagementSystem.students:
            print("\nNo students to display.")
        else:
            print("\n" + "-" * 30)
            print(f"{'Student List':^30}")
            print("=" * 30)
            index = 1
            for student in StudentManagementSystem.students:
                print(f"\nStudent {index}")
                print("-" * 30)
                print(f"Name: {student['name']}")
                print(f"ID: {student['id']}")
                print(f"Department: {student['department']}")
                print(f"Degree: {student['degree']}")
                print("-" * 30)
                index += 1

    def search_student(self):
        roll = input("\nEnter the ID you want to search: ")
        found = [student for student in StudentManagementSystem.students if student["id"] == roll]
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

    def edit_student(self):
        id = input("Enter the student ID you want to edit: ")
        for student in StudentManagementSystem.students:
            if student["id"] == id:
                new_name = input("Enter New Name: ")
                new_department = input("Enter New Department: ")
                new_degree = input("Enter New Degree: ")
                new_id = input("Enter New ID: ")
                student.update({"name": new_name, "id": new_id, "department": new_department, "degree": new_degree})
                self.save_students()
                print("\nStudent profile updated successfully!")
                return
        print("\nStudent not found.")

    def delete_student(self):
        id = input("Enter the student ID you want to delete: ")
        for student in StudentManagementSystem.students:
            if student["id"] == id:
                StudentManagementSystem.students.remove(student)
                self.save_students()
                print("\nStudent has been removed.")
                return
        print("\nStudent not found.")


system = StudentManagementSystem()
system.load_students()

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
        system.add_student()
    elif choice == "2":
        system.view_all_students()
    elif choice == "3":
        system.search_student()
    elif choice == "4":
        system.edit_student()
    elif choice == "5":
        system.delete_student()
    elif choice == "6":
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Try again.")
