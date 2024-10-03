#Write a Python program to sort a list alphabetically in a dictionary. 
num_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} 
#'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

for i in num_dict:
    num_dict[i].sort()
print(num_dict)