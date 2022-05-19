class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def getprice(self):
        return self.price


b1 = Book("war and peace", 12)
b2 = Book("The princess", 32)

print(b1.price, b1.title)
print(b2.title, b2.price)
print(b1.getprice())
print(b2.getprice())
