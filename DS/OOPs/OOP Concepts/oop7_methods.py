"""
MRO for methods
Super constr
super method

"""
'''
class A:

    def __init__(self):
        print("in A INIT")

    def feature1(self):
        print("Feature 1-A working")

class B: #Single inheritance
    def __init__(self):
        #super().__init__()
        print("in B init")

    def feature1(self):
        print("Feature 1-B working")

class C(B,A):
    def __init__(self):
        #super(C, self).__init__()
        super().__init__()
        print("in C init")


#a=A()
b=C()
b.feature1()
op:
in B init
in C init
Feature 1-B working
'''


class A:

    def __init__(self):
        print("in A INIT")

    def feature1(self):
        print("Feature 1-A working")

class B: #Single inheritance
    def __init__(self):
        #super().__init__()
        print("in B init")

    def feature1(self):
        print("Feature 1-B working")

class C(A,B):
    def __init__(self):
        #super(C, self).__init__()
        super().__init__()#super constructor
        print("in C init")

    def feat(self):
        super().feature1()#super method

c=C()
c.feature1()
c.feat()

# op:
# in A INIT
# in C init
# Feature 1-A working



