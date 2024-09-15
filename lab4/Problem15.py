#Apply various functions like append, remove, pop, insert, sort, max, min in a list.
l=[1,2,7,4,8,9,10]
l.append(17)
l.append(11)
l.append(12)
print("the removed item is",l.pop())
l.remove(9)
l.sort()
print("the sorted list is",l)
print("the greatest number of the list is",max(l))
print("the smallest numeber in the list is",min(l))
l.insert(2,"hi")
print("The list after insert() function is",l)
