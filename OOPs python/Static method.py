
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    @staticmethod     # decorator
    def hello():
        print("hello")

s1=Student("Umar",[83,67,78])
print(s1.name,s1.marks)
s1.hello()

