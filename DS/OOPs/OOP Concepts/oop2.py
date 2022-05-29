"""
Constructores and Comparing Objects
"""

class computer:
    def __init__(self):
        self.name="Balaji"
        self.age=23

    def compare(self,other):
        if self.age==other.age:return True
        else:return False

#address of memeory 1903586265936
c1=computer()
c1.age=32
c2=computer()
if c1.compare(c2):
    print("equal")
else:
    print("Not equal")

print(c1.name)
print(c2.name)
