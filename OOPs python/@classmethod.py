class Person:
    name="rehan"
   # def changename(self,name):             manual tor pr  is method sy b chage ho skta ha
    #    self.__class__.name="hamid"

    @classmethod
    def changename(cls,name):
        cls.name=name


p1=Person()
p1.changename("Header")
print(p1.name)        
print(Person.name)