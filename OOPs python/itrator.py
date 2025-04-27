class Mynumbers:
    def __iter__(self):       # jis program my only __iter__ use ho us ko itrable 
                              # age __iter__ ky sath __next__ dono ka use hon us ko itrator khty ha
        self.a=1
        return self
    
    def __next__(self):
        x=self.a         # itrator ki value kisi na kisi object my store krwani hoti ha jo ky x my ha x ak object ha 
        self.a+=1
        return x

myclass=Mynumbers()
myiter=iter(myclass)   

print(next(myiter))    # next ka function hi value ko agy print krwata ha 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))