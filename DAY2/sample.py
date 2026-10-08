x=int(input("enter a number:\n"))


for i in range(x//2+1):
    for j in range(i):
        print("*",end="")
    for k in range(x-2*i+1):
        print(" ",end="")
    for p in range(i):
        print("*",end="")
    print("\n")
print("*"*(x+1))
for i in range(x//2+1):
    for j in range(x-3*i-1):
        print("*",end="")
    for k in range(2*i+1):
        print(" ",end="")
    for p in range(x-3*i-1):
        print("*",end="")

    print("\n")

    

        
   
