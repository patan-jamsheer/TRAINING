class ComplexNumber:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,obj2):
        return ComplexNumber(self.real+obj2.real,self.img+obj2.img)
    def display(self):
        print(str(self.real) + "i +" +str(self.img) +"j")
    



cn1=ComplexNumber(1,2)
cn1.display()
cn2=ComplexNumber(3,4)
cn2.display()

cn3=cn1+cn2
cn3.display()