'''
Constructor in Inheritance
Method resolution order(MRO)
Super constr


'''
"""
class A:

    def __init__(self):
        print("in a INIT")

    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B(A): #Single inheritance
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("feature 4 working")

#a=A()
b=B()#since it is inherited rom A constrc of A is called when obj for B is created
output:in a INIT
"""
"""
class A:

    def __init__(self):
        print("in a INIT")

    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B(A): #Single inheritance
    def __init__(self):
        print("in B init")

    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("feature 4 working")

#a=A()
b=B()#since B has an init it wont call A init Instead it calls B init
output:
in B init

"""
'''
class A:

    def __init__(self):
        print("in a INIT")

    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B(A): #Single inheritance
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("feature 4 working")



#a=A()
b=B()#It calls first B init and calls A init as we used super()
output:
in a INIT
in B init

'''

class A:

    def __init__(self):
        print("in A INIT")

    def feature1(self):
        print("Feature 1 working")

class B: #Single inheritance
    def __init__(self):
        #super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

class C(B,A):
    def __init__(self):
        #super(C, self).__init__()
        super().__init__()
        print("in C init")


#a=A()
b=C()#It calls first B and then C because it follows L->R(MRO)
output:
in B init
in C init



