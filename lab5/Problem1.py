#Write a Python program to convert a tuple to a string. 
t=(1,2,"hi")
st=''
for i in t:
    st=st+str(i)
print(st)