# Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class. 

class Student:
    def __init__(self, student_id, student_name=None, student_class=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def student_data(self):
        print(f"Student ID: {self.student_id}")
        if self.student_name:
            print(f"Student Name: {self.student_name}")
        if self.student_class:
            print(f"Student Class: {self.student_class}")

student2 = Student(102, student_name="John Doe")
student2.student_data()

print()

student3 = Student(103, student_name="Jane Doe", student_class="10th Grade")
student3.student_data()
