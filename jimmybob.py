from Bicycle import Bike
from Car import Car


def main():
    c1 = Car("Toy", "super", "Blue", "Super toy blue car", "George")
    c1.print()
    print("Car 1 started")
    c1.start()
    c1.print()
    b1 = Bike("Mountain", "Red", "Red Mountain Bike", "steve")
    b1.print()
    b1.pedal()
    b1.print()


main()
