from abc import ABC, abstractmethod
from Wheels import Wheels


class Vehicle(ABC):
    def __init__(self, make, color, name, owner):
        self.make = make
        self.color = color
        self.name = name
        self.owner = owner
        self.wheel_type = Wheels(-1.0)

    def print(self):
        pass