"""
Method OverLoading->two methods insde a sam eclassbut different arguments
Method OverRiding->
"""

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,n1=None,n2=None,n3=None):#method overloading block
        if n1!=None and n2!=None and n3!=None:
            return n1+n2+n3
        elif n1!=None and n2!=None:
            return n1+n2
        else:
            return n1


o1=Student(1,2)
print(o1.sum(2))
