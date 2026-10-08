import random
from random import *
def generate_otp():
    otp=""
    for i in range(4):
        otp+=str(randint(0,9))
    return int(otp)

print("-"*50)
print("OTP GENERATED  IS:",generate_otp())
print("-"*50)









