class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,obj2):     # __add__ ya ak dunder function ha isi ki wja sy program run ho ga 
        newReal=self.real+num2.real  
        newimg=self.img+num2.img
        return Complex(newReal,newimg)   
    
    def __sub__(self,obj2):    #__sub__ ya ak dunder function ha isi ki wja sy program run ho ga 
        newReal=self.real-num2.real  
        newimg=self.img-num2.img             # isi trha mul,div,modulus b ly skty ha
        return Complex(newReal,newimg)  

num1=Complex(3,5)
num1.shownumber()                   #      ya sara function operator overloading ko define krta ha 
                                       # jis my hm koi b opr ko overload yani change kr skty ha us ka mtlb hi change ho jata ha
num2=Complex(4,8)        
num2.shownumber()

num3=num1+num2
num3.shownumber()

num3=num1-num2
num3.shownumber()
