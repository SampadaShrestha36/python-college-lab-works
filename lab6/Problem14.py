#Write a Python script to check whether a given key already exists in a dictionary. 
d={'name':'Hari','age':'29','city':'Bhaktapur','workplace':'Bhaktapur'}
n=input("Enter the key")
if n in d:
    print("The key already exists")
else:
    print("The key does not exist")