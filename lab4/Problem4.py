#Write a Python program to find the second smallest and second largest numbers in a list.
l=[10,20,40,12,234,534,23,1]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(f"second smallest={l[1]} and second largest={l[len(l)-2]}")