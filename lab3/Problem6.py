#Write a Python program to guess a number between 1 and 9. Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit. Import random. 
import random
while(True):
    n=random.randint(1,10)
    i=int(input("Enter a number between 1 and 9"))
    if(i==n):
        print("Well Guessed!")
        exit()
