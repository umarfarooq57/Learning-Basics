# create student slass that takes name & msrks of 3 subjects as argumentes  in  comstructure. 
# then create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi ",self.name," your average score is: ",sum/3)    


s1=Student("Tony stark",[99,98,97])   
s1.get_avg() 

s1.name="ironman"      # change name
s1.get_avg()

