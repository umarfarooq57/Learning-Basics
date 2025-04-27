class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi",self.name," your subjects Avarage score is : ",sum/3)

s1=Student("Umar",[83,67,78])
s1.get_avg()

s1.name="Fahed"     # name change
s1.get_avg()


