class Student:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    @property
    def percentage(self):
        print(str((self.a+self.b+self.c)/3)+"%")
s1=Student(100,100,100)
s1.percentage
s1.a=50
s1.percentage