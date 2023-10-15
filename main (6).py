class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
student1 = Student("Alice", "S123", 3.7)
student2 = Student("Bob", "S124", 3.9)
student3 = Student("Charlie", "S125", 3.5)
student4 = Student("David", "S126", 3.8)

students = [student1, student2, student3, student4]
