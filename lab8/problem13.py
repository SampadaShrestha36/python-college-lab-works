# Write a Python function that takes a name (string) as argument and capitalizes the first and fourth letters of the input name. 
def capital(s):
    l=[]
    a=""
    for i in s:
        l.append(i)
    l[0]=l[0].upper()
    l[3]=l[3].upper()
    for i in l:
        a=a+i
    return a
print(capital(input("enter a string")))