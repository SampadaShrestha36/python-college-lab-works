# Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values.
class Student:
    student_id=790336
    student_name='Sampada'
    
    def student_data(self):
        if hasattr(self, 'student_name'):  # Check if student_name exists
            print(self.student_name)
        if hasattr(self, 'student_class'):  # Check if student_class exists
            print(self.student_class)
        print(self.student_id)

s1=Student()
s1.student_class='BE'
s1.student_data()
del Student.student_name
s1.student_data()