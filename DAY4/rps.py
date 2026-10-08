import random
from random import *

list=["rock","papper","scissor"]
def rps():
    while True:
        computer=randint(0,2)
        print("1.rock\n2.papper\n3.scissor\n")
        user_c=int(input("enter your choice\n"))
        
        user_c-=1
        if user_c==computer:
            print("TIE\n")
        elif user_c==0 :
            if computer==1:
                print("computer won\n")
            else:
                print("hurray you won\n")
        elif user_c==1:
            if computer==0:
                print("hurray you won\n")
            else:
                print("computer won\n")
        elif user_c==2:
            if computer==0:
                print("computer won\n")
            else:
                print("hurray you won\n")
rps()

