class BooK:
    def __init__(self, title, price, author, pages):
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages


class Magazine:
    def __init__(self, title, price, period, publisher):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher


class Newspaper:
    def __init__(self, title, price, period, publisher):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher


b1 = BooK("B@C", 23.0, "Bala", 102)
m1 = Magazine("CBC", 45.0, "Weekly", "Buddu")
n1 = Newspaper("Hindu", 4, 'Daily', 'Chandu')


print("**********************************")
print(b1.title, b1.price, b1.author, b1.pages)
print(m1.title, m1.price, m1.period, m1.publisher)
print(n1.title, n1.price, n1.period, n1.publisher)

print("**********************************")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
print("**********************************")
