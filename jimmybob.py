class wheels:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return str(self.radius)
    

class car:
    def __init__(self, model, make, color, name, owner):
        self.model = model
        self.make = make
        self.color = color
        self.name = name
        self.owner = owner
        self.on = False
        self.wheel_type = wheels(50.0)

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def print(self):
        print(f"Car, {'Running' if self.on else 'Stopped'}\n\tModel: {self.model}\n\tMake: {self.make}\n\tColor: {self.color}\n\tName: {self.name}\n\tOwner: {self.owner}\n\tWheel Radius: {self.wheel_type}")


class bike:
    def __init__(self, make, color, name, owner):
        self.make = make
        self.color = color
        self.name = name
        self.owner = owner
        self.zoomin = False
        self.wheel_type = wheels(10.5)

    def pedal(self):
        self.zoomin = True

    def stop(self):
        self.zommin = False

    def print(self):
        print(f"Bicycle, {'Zoomin' if self.zoomin else 'Not Zoomin'}\n\tMake: {self.make}\n\tColor: {self.color}\n\tName: {self.name}\n\tOwner: {self.owner}\n\tWheel Radius: {self.wheel_type}")


def main():
    c1 = car("Toy", "super", "Blue", "Super toy blue car", "George")
    c1.print()
    print("Car 1 started")
    c1.start()
    c1.print()
    b1 = bike("Mountain", "Red", "Red Mountain Bike", "steve")
    b1.print()
    b1.pedal()
    b1.print()


main()
