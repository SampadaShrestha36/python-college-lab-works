#Write a Python program to create an intersection, a union, set difference and a symmetric difference of sets. Also find the length, maximum and minimum values in a set. 
a={1,2,3,4,5,6,7,8}
b={0,4,7,8,12,9,43}
print("union=",a|b)
print("intersection=",a&b)
print("difference=",a-b)
print("symmetric_difference=",a^b)
print("The length of first and second tuple is",len(a),len(b))
print("The max and min value of first set is",max(a),min(a))