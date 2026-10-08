class Animal:
    def make_sound(self):
        print("aniaml is making sound")
class Dog(Animal):
    def make_sound(self):
        print("-"*50)
        print("Dog is Barking")
        print("-"*50)
class Cat(Animal):
    def make_sound(self):
        print("-"*50)
        print("Cat is Meowing")
        print("-"*50)
class Cow(Animal):
    def make_sound(self):
        print("-"*50)
        print("Cow is Mooing")
        print("-"*50)
dog1=Dog()
dog1.make_sound()
cat1=Cat()
cat1.make_sound()
cow1=Cow()
cow1.make_sound()












