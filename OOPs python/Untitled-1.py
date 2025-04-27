# simple define  
class Car:
    name = "Odi"
    color="Blue"
    model=2018

    
    def __init__(self): 
       print("car types....")
       self.car=Car

        
car1=Car()
print(car1.name,car1.color,car1.model)   

#   constructor type 

class Student:

        def __init__(self,name,age): 
            print("Adding a new student in database..")
            self.name= name
            self.Age=age


s1=Student("essa",23)
print(s1.name,s1.Age)

s2=Student("Musa",34)
print(s2.name,s2.Age)

