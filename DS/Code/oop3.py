class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price-(self.price*self._discount)
        else:
            return self.price
        # return self.price

    def setprice(self, amount):
        self._discount = amount


b1 = Book("war and peace", 12)
b2 = Book("The princess", 32)

# print(b1.price, b1.title)
# print(b2.title, b2.price)
# print(b1.getprice())
# print(b2.getprice())

print(b1.getprice())
b1.setprice(0.5)
print(b1.getprice())
print(b1._discount)
