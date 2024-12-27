# Modify above function so that it has default values of 2 for both length and width.
def ap(l=2,w=2):
    a=l*w
    p=2*(l+w)
    return a,p
l,w=int(input("enter the length and width of rectangle")),int(input())
a,p=ap()
print(f"area={a} and perimeter={p}")
a,p=ap(l)
print(f"area={a} and perimeter={p}")
a,p=ap(l,w)
print(f"area={a} and perimeter={p}")