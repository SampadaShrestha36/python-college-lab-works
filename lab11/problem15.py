#  Ram has used a text editing software to type some text. After saving the article as WORDS.TXT, she realized that she has wrongly typed alphabet J in place of alphabet I everywhere in the article. Write a function definition for JTOI() in Python that would display the corrected version of entire content of the file WORDS.TXT with all the alphabets "J" to be displayed as an alphabet "I" on screen. Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.

def JTOI():
    f = open("WORDS.txt","r+")
    a=f.read()
    f.seek(0)
    f.write(a.replace("J","I"))
    f.seek(0)
    print(f.read())
    f.close()
JTOI()
