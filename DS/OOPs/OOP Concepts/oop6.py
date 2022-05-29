"""
Inheritance

1)single
2)multilevel
3)multiple
"""
class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B: #Single inheritance
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("feature 4 working")

class C:
    def feature5(self):
        print("Feature C working")

'''
class C(B):
    def feature5(self):
        print("Feature C working")'''

class D(A,B,C):#multiple
    pass

a1=A()
a1.feature1()
a1.feature2()
'''
b1=B()
b1.feature4()
b1.feature3()
b1.feature1()

c1=C()
c1.feature5()
'''
d1=D()
d1.feature1()
d1.feature3()
d1.feature5()
