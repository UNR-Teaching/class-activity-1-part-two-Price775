from Vehicle import Vehicle
from Wheels import Wheels

class Bike(Vehicle):
    def __init__(self, make, color, name, owner):
        super().__init__(make, color, name, owner)
        self.zoomin = False
        self.wheel_type = Wheels(10.5)

    def pedal(self):
        self.zoomin = True

    def stop(self):
        self.zommin = False

    def print(self):
        print(f"Bicycle, {'Zoomin' if self.zoomin else 'Not Zoomin'}\n\tMake: {self.make}\n\tColor: {self.color}\n\tName: {self.name}\n\tOwner: {self.owner}\n\tWheel Radius: {self.wheel_type}")
