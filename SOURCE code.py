# School-Management-system
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class SchoolManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.roll_number] = student

    def remove_student(self, roll_number):
        if roll_number in self.students:
            del self.students[roll_number]

    def display_students(self):
        for roll_number, student in self.students.items():
            print(f"Roll Number: {roll_number}, Name: {student.name}, Grade: {student.grade}")

# Example usage:
student1 = Student("John Doe", "101", "A")
student2 = Student("Jane Smith", "102", "B")

school_system = SchoolManagementSystem()
school_system.add_student(student1)
school_system.add_student(student2)

school_system.display_students()

school_system.remove_student("101")
print("\nAfter removing student with Roll Number 101:")
school_system.display_students()
