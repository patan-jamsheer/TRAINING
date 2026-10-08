from random import *


def guess():
    x=randint(1,10)
    while True:
        try:
            g_no=int(input("guess the number between 1-10\n"))
        except ValueError:
            print("enter only digits from 1-10\n")
            continue
        if 1<=g_no<=10:
            if g_no==x:
                print("Hurray successfully guessed\n")
                break
            else:
                print("Incorrect Guess Try Again\n")
        else:
            print("invalid range\n")




guess()