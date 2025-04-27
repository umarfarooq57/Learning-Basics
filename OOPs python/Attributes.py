class Student():
    college_name="ABC College"
    name="karan"            # class attr 
    def __init__(self,name,marks):             
        self.name=name   # object attr > class attr
        self.marks=marks
        print("Addition new student in Database..")    
s1=Student("Umar",100)
print(s1.name,s1.marks)  
