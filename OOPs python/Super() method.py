class Car:
        def __init__(self,type):
            self.type=type

        @staticmethod
        def start():
            print("Car started..")

        @staticmethod
        def stop():
            print("Car stoped..")  


class Toyotacar(Car):     
    def __init__(self,name,type):
        super().__init__(type)     # super() ka method hi ak class my data ko dosri class sy access krta
        self.name=name           #  ha agr us class my koi type na di jay
        super().start()     # agr hm car start krna chey tu super ka method use kr skty ha

car1=Toyotacar("Prius","Electric") 
print(car1.name) 
print(car1.type)  



print(car1.stop())   