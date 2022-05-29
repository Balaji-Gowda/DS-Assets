"""
Method OverRiding
"""
class A:

    def show(self):
        print("in A Show")

class B(A):
    #######overridfing take splace like if i dont have show in B then A's show will be called else if B has the B's show will be primted
    def show(self):
        print("inside B Show which was overriden A show method")

b=B()
b.show()
