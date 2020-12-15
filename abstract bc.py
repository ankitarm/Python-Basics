# abstract base class
# the printarea method is forced complusary to be created by abstract class in the subclasses
# shape class forcing the other subclasses to create printarea  method
from abc import ABC, abstractmethod
# abc module, abc meta class instructs to some methods to implement complusary

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length=5
        self.breadth=6

    def printarea(self):
        return self.length*self.breadth


r = Rectangle()
print(r.printarea())
# u cant make object of abtract base class
# s = Shape()