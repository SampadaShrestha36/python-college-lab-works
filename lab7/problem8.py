# Write a Python function to find the maximum and minimum value, sum and multiplication of all the numbers in a list. 
def func(l):
    s=0
    m=1
    for i in l:
        s=s+i
        m=m*i
    return s,m,min(l),max(l)
l=[1,2,3,4,5,6,7,8,9]
s,m,min,max=func(l)
print(f"sum={s}, multiplication={m}, min={min}, max={max}")