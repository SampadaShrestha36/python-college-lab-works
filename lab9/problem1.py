# Define a Python function student(). Using function attributes display the names of all arguments.

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def student(self):
        print(self.name,self.roll)
s1=Student('Sampada',790336)
s1.student()