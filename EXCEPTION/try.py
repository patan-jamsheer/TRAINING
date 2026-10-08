number=input("enter a number")

print(f"multiplication Table of {number} is\n")
try:
    for i in range(11):
        print(f"{int(number)} X {i} = {int(number)*i}\n")
except Exception as e:
    print(e)

print("some lines of code\n")
print("end of the programe\n")















