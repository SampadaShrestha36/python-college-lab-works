# Write a python function that takes two parameters length and width and returns the area and perimeter of a rectangle.
def ap(l,w):
    a=l*w
    p=2*(l+w)
    return a,p
l,w=int(input("enter the length and width of rectangle")),int(input())
a,p=ap(l,w)
print(f"area={a} and perimeter={p}")