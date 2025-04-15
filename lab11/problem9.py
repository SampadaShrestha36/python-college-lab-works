# Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the". 
def func():
    f = open("notes.txt","r")
    a=1
    for i in f.readlines():
        b=1
        for j in i.split():
            if j.lower() == "the":
                print("The is present in Line number",a,"and word number",b)
            b=b+1
        a=a+1
    f.close()
func()
