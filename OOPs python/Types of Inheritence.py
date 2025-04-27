# there are three basics types inheritence 
# single type
# multi type
# multiple type


class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stoped..")  


class Toyotacar(Car):     
    def __init__(self,brand):
        self.name=brand


class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type
frn1=Fortuner("Desil")
print(frn1.start())    #multi class type



