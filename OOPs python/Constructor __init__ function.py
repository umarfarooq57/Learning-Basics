# all clases have a function called __init__(),which is always executed when the objects ids being initiated

class Student():
    name="Umar"
    def __init__(self):   # self basically hmy student ka object location store krwa rha ha 
        # jb b program run hota ya def function sb sy phly check kiya jata ha 
        print(self)
        print("Adding new student in database..")

s1=Student()   
print(s1)    

print("_______________Next________________________")



class Student():

# define constructure
    def __init__(self):              
        print("Addition new student i database..")
    # this is parameterized constructure
    def __init__(self,name,marks):              # self ak reference ha 
        self.name=name
        self.marks=marks
        print("Addition new student in Database..")    #    This is a constructure
s1=Student("Umar",100)
print(s1.name,s1.marks)  

s2=Student("Farooq",80)
print(s2.name,s2.marks)

# jinta b data store kiya jata ha is ko attribute khty ha
