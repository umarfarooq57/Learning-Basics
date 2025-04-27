# it is changing method to need of person  data

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def persantage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"   
    

stu1=Student(87,98,76)
print(stu1.persantage)

stu1.phy=67
print(stu1.phy)
print(stu1.persantage)