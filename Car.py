from Vehicle import Vehicle
from Wheels import Wheels

class Car(Vehicle):
    def __init__(self, model, make, color, name, owner):
        super().__init__(make, color, name, owner)
        self.model = model
        self.wheel_type = Wheels(50.0)
        self.on = False

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def print(self):
        print(f"Car, {'Running' if self.on else 'Stopped'}\n\tModel: {self.model}\n\tMake: {self.make}\n\tColor: {self.color}\n\tName: {self.name}\n\tOwner: {self.owner}\n\tWheel Radius: {self.wheel_type}")
