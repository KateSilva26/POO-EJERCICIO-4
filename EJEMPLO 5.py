
class Car:
    __maxspeed = 0
    name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self.name = "SuperCar"
        
    def drive(self):
        print("Driving Maxspeed: ", self.__maxspeed)
        
    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

bluecar = Car()
bluecar.drive()
bluecar.setMaxSpeed(400)
bluecar.drive()
