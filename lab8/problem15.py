#  Write a Python function takes a two-word strings and find if both words begin with same letter or not.
def func(s1,s2):
    if s1[0].lower()==s2[0].lower():
        print("They begin with same letter")
    else:
        print("They do not begin with same letter")
s1,s2=input("Enter two strings"),input()
func(s1,s2)