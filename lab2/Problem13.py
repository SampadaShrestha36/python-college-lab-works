#Write a python script that takes a letter grade (A, B, C, D, F) as input and prints the bcorresponding grade point average (GPA). For example, A = 4.0, B = 3.0, C = 2.0, D = 1.0, F=0.0. Include an else statement to handle invalid inputs.
grade=input("Enter the grade")
grade=grade.upper()
d={"A":4.0,"B":3.0,"C":2.0,"D":1.0,"F":0.0}
if grade in d:
    print("GPA: ",d[grade])
else:
    print("Invalid input")
