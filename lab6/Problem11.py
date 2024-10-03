#Write a Python program to find all keys in a dictionary that have the given value. 
d={'name':'Hari','age':'29','city':'Bhaktapur','workplace':'Bhaktapur'}
for i in d:
    if d[i]=="Bhaktapur":
        print(i)
# for x,y in d.items():
#     if y=="Bhaktapur":
#         print(x)