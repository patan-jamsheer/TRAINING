operator=int(input("enter the operator"))
grade=""
if operator>=90:
    grade="A"
elif operator>=80:
    grade="B"
elif operator>=70:
    grade="C"
elif operator>=60:
    grade="D"
elif operator>=50:
    grade="E"
if len(grade)==0:
    print("person is failed")
else:
    print(f"person secured the grade ={grade}")
