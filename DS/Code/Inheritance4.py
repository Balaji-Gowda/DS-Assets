class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.boo = "boo"
        self.name = "class B"

    def met(self):
        print("this cls B method")


class C(B, A):
    def __init__(self):
        super().__init__()

    def showpars(self):
        print(self.foo)
        print(self.boo)
        print(self.name)
        # B.met(self)


c = C()
c.showpars()
print(C.mro())
print()
