class Book:
    def __init__(self, name):
        self.name = name


class Newspaper:
    def __init__(self, name) -> None:
        self.name = name


b1 = Book("Physics")
b2 = Book("Maths")
n1 = Newspaper("Hindu")
n2 = Newspaper("Vaartha")

print(type(b1) == type(b2))  # true
print(type(b1) == type(n1))  # false
print(type(b2) == type(n2))  # false

print(isinstance(b1, Book))  # T
print(isinstance(n1, Newspaper))  # T
print(isinstance(b2, Book))  # T
print(isinstance(b2, Newspaper))  # F
