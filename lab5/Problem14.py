#Write a Python program to find the longest common prefix of all strings. Use the Python set.
s = ["setasdfsa", "sentence", "seagul"]
common_prefix = ""
min_len = len(min(s, key=len))
for i in range(min_len):
    char_set = set()  
    for word in s:
        char_set.add(word[i])
    if len(char_set) == 1:
        common_prefix += s[0][i]
    else:
        break  
print(common_prefix)  


