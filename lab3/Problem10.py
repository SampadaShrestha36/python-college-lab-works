#Write a Python program to develop a rock paper scissors game, restart the game until the user press ‘n’ when the game ends. 
import random
l=["Rock", "Paper","Scissors"]
while True:
    s=random.choice(l)
    n=input("Rock, paper or scissors")
    a=n.capitalize()
    if a not in l:
        print("Invalid input!")
    else:
        print("computer chose",s)
        if a == s:
            print("It's a tie!")
        elif (a == "Rock" and s == "Scissors") or (a == "Scissors" and s == "Paper") or (a == "Paper" and s == "Rock"):
            print("You win!")
        else:
            print("You lose :(")
        c=input("Do you want to continue?(y/n)")
        b=c.lower()
        if b=="y":
            pass
        elif b=="n":
            exit()
        else:
            print("Invalid input")
