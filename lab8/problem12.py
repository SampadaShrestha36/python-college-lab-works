# Write a Python function that takes a date in string format DD/MM/YYYY and checks if it is a valid date and in the correct format. 
def func(s):
    if s[2]=='/' and s[5]=='/' and s[-5]=='/':
        if int(s[0]+s[1])<=30 and int(s[3]+s[4])<=12:
            print("valid date")
        else:
            print("Invalid date")
    else:
        print("Invalid date")

s=input("enter the date")
func(s)