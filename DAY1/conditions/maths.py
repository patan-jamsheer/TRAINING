
print("1)+ 2)- 3)* 4)% 5)^")
operator=input("enter an operator")
a=int(input("enter first number"))
b=int(input("enter first number"))

if operator=="+":
    print(f"sum of a+b={a+b}")
elif operator=="-":
    print(f"subtraction of a-b={a-b}")
elif operator=="*":
    print(f"multiplication of a*b={a*b}")
elif operator=="%":
    print(f"modulo of a%b={a%b}")
elif operator=="^":
    print(f"power of a^b={a^b}")
else:
    print(f"Invalid operator")
