#question1
print("question 1")
string=input("enter  your name")
print(string[::-1])

#question 2
print("question 2")

upper=0
lower=0
for i in range(len(string)):
    if string[i].isupper():
        upper+=1
    elif string[i].islower():
        lower+=1
print(f"No of upper case letter ={upper}")
print(f"No of lower case letter ={lower}")



#question 3
print("question 3")

if string.isdigit():
    print("yes the string is contained of all digits")
else:
    print("no the string is not contained of all digits")
   
#question 4
print("question 4")

print(string.replace(" ","_"))

#question 5
print("question 5")

dict={}
for i in range(len(string)):
    if string[i] not in dict:
        dict[string[i]]=0
    else:
        dict[string[i]]+=1
print(dict)






