class Student:
    name="anonymous"
    def __init__(self,name):
        self.name=name
    @classmethod
    def changename(cls,name):
        cls.name=name
    @staticmethod
    def method():
        print("Iam just a static method")





#classmethod->modifies the class attributes
#staicmethod->doesnot interfere the class or object attributes
#normal methods->modifies the object attributes
s1=Student("jaheer")
s1.changename("jamsheer")
print(s1.__class__.name)