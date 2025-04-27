class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started...")

    def stop(self):
        self.brk=True
        print("Car stop...")    

car1=Car()
car1.start()        

car1.stop()
