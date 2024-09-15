# Write a Python Program to sort a list of lists by a given index of the inner list.
l = [[1, 2, 3, 4], [29, 34, 5, 60], [23, 45, 34, 12]]
n = int(input("Enter the index of the inner list to sort the list of lists: "))
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i][n] > l[j][n]:
            l[i], l[j] = l[j], l[i]

print(l)


