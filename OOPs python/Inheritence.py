# ak class ky data ko dosri class my pass krwana 

class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stoped..")  

class Toyota(Car):     # ak class ka data dosry my krwany ky liya sirf us class ka object likhna ha bracket my
    def __init__(self,name):
        self.name=name

car1=Toyota("fortuner")
car2=Toyota("prius")
print(car1.name)
print(car2.name)

print(car1.start())

print(car1.color)