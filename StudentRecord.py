from pip._vendor.rich.prompt import Prompt 


class StudentRecord:
    def __init__(self, name, father_name, subject, marks, contact_number):
        self.name = name
        self.father_name = father_name
        self.subject = subject
        self.marks = marks
        self.contact_number = contact_number
        self.percentage = self.calculate_percentage()

    def calculate_percentage(self):
        return (sum(self.marks) / (len(self.marks) * 100)) * 100

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Father's Name: {self.father_name}")
        print(f"Subject: {self.subject}")
        print(f"Marks: {self.marks}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Contact Number: {self.contact_number}")


class StudentDatabase:
    def __init__(self, password):
        self.students = {}
        self.password = password

    def authenticate(self):
        input_password = Prompt.ask("Enter password to access records", password=True)
        return input_password == self.password

    def add_student(self, name, father_name, subject, marks, contact_number):
        if name in self.students:
            print("Student already exists.")
        else:
            student = StudentRecord(name, father_name, subject, marks, contact_number)
            self.students[name] = student
            print("Student added successfully.")

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def show_student_details(self, name):
        if name in self.students:
            print("\nStudent Details:")
            self.students[name].display_details()
        else:
            print("Student not found.")

    def show_all_students(self):
        if not self.students:
            print("No student records available.")
        else:
            print("\nAll Students Records:")
            for student in self.students.values():
                student.display_details()
                print("-" * 20)


def main():
    database_password = "polyne254" 
    student_db = StudentDatabase(database_password)

    if not student_db.authenticate():
        print("Access denied. Incorrect password.")
        return

    while True:
        print("\nStudent Records Management")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Show Student Details")
        print("4. Show All Students")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Enter student's name: ").strip()
            father_name = input("Enter father's name: ").strip()
            subject = input("Enter subject: ").strip()
            try:
                marks = list(map(int, input("Enter marks separated by spaces: ").strip().split()))
            except ValueError:
                print("Invalid marks input. Please enter space-separated integers.")
                continue
            contact_number = input("Enter contact number: ").strip()
            student_db.add_student(name, father_name, subject, marks, contact_number)

        elif choice == "2":
            name = input("Enter student's name to delete: ").strip()
            student_db.delete_student(name)

        elif choice == "3":
            name = input("Enter student's name to view details: ").strip()
            student_db.show_student_details(name)

        elif choice == "4":
            student_db.show_all_students()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
