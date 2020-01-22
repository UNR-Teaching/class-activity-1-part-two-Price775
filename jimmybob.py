class car:
    def __init__(self, model, make, color, name, owner):
        self.model = model
        self.make = make
        self.color = color
        self.name = name
        self.owner = owner
    def print(self):
        print(f"Car\n\tModel: {self.model}\n\tMake: {self.make}\n\tColor: {self.color}\n\tName: {self.name}\n\tOwner: {self.owner}")


class bike:
    def __init__(self, make, color, name, owner):
        self.make = make
        self.color = color
        self.name = name
        self.owner = owner
    def print(self):
        print(f"Bicycle\n\tMake: {self.make}\n\tColor: {self.color}\n\tName: {self.name}\n\tOwner: {self.owner}")
def main():
    c1 = car("Toy", "super", "Blue", "Super toy blue car", "George")
    c1.print()
    b1 = bike("Mountain", "Red", "Red Mountain Bike", "steve")
    b1.print()


main()
