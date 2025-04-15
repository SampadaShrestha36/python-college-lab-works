# Write a function in python to write then read the content from a text file "poem.txt" line by line and display the same on screen.

f = open("poem.txt","w")
f.write('''Because I could not stop for Death
He kindly stopped for me
The Carriage held but just Ourselves
And Immortality.''')
f.close()

f = open("poem.txt","r")
for line in f.readlines():
    print(line)
