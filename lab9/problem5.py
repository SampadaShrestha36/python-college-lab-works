# Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class. 
class Student:
    student_id=790336
    student_name='Sampada'
    
    def student_data(self):
        print(self.student_name)
        if hasattr(self, 'student_class'):  # Check if student_class exists
            print(self.student_class)
        print(self.student_id)

s1=Student()
s1.student_class='BE'
s1.student_data()
