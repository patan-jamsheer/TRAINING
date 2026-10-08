pass_count=3
real_password="1234"
locked=False
print("-"*50)
while pass_count>0 and locked ==False:
    
    if locked ==False:
        password=input("enter the password")
        if password==real_password:
            print("-"*50)
            print("hurray unlocked \n")
            break
        else:
            print("-"*50)

            print("incorrect password \n")
            pass_count-=1
            print(f"Attempts left={pass_count}\n")
            print("-"*50)

            if pass_count<=0:
                locked=True

                print(" LOcked \n Not possible to unlock \n")
                print("-"*50)

    else:
        print("Locked \n")
