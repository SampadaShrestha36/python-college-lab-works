#  Defines a function called calculate_average that takes a list of numbers as input and calculate the average of list. Finally, the function returns the average of that list.
def calculate_average(l):
    s=0
    for i in l:
        s=s+i
    return s/len(l)
l=[1,2,3,4,5,6,7,8,9]
print("The average is",calculate_average(l))