class Student:
    def __init__(self,name:str,roll_no:int,branch:str,age:int,marks:int):
        self.name:str=name
        self.roll_no:int=roll_no
        self.branch:str=branch
        self.age:int=age
        self.marks:int=marks
    def display_details(self):
        print(f"NAME:{self.name}\n ROLL_NO:{self.roll_no}\n BRANCH:{self.branch}\n AGE:{self.age}\nMARKS:{self.marks}")

s1=Student("jamsheer",42,"AI-ML",21,100)
s1.display_details()