#Write a  Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,20,20]
n = 0
checked_pairs = set() 

for i in range(len(s)):
    for j in range(len(s)):
        if i!=j and (s[i], s[j]) not in checked_pairs and (s[j], s[i]) not in checked_pairs:
            checked_pairs.add((s[i], s[j]))
            if s[i] * s[j] > n:
                n = s[i] * s[j]
                a = s[i]
                b = s[j]

print(f"The numbers are {a} and {b}")
