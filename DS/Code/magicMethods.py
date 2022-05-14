class Book:
    def __init__(self, title, price, pages):
        self.title = title
        self.price = price
        self.pages = pages

    def __eq__(self, val):
        if(self.price == val.price or self.pages == val.pages):
            return True
        else:
            return False

    def __str__(self):
        return (f"{self.price}, {self.title}, {self.pages}")


o1 = Book("Skill Voila", 32, 100)
o2 = Book("top mentor", 30, 100)
o3 = Book("Skill Voila", 32, 100)

print(o1 == o2)
print(o1)
# o1
sr = "hEy HI"
print(sr)
