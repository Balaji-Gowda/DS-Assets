from abc import ABC, abstractmethod


class Graphicshape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(Graphicshape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return self.radius*self.radius*3.14


class Square(Graphicshape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return self.radius*self.radius


# g = Graphicshape()
c = Circle(10)
print(c.radius)
print(c.calcArea())
s = Square(12)
print(s.radius)
print(s.calcArea())


# It tells that we shouldn't instatiate abs base class and
# We need to overwrite abs method of ABC in its inherited sub class
