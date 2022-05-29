"""
Types of methods
methods are three types
1) class
2) instance
3) static -> which has no concern about instance or class variables



Accessors- get methods
mutators- set methods

Decorartors-calssmethod-to indicate its an classs method
"""
class Student:
    school="CTS"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):#instance method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):#Accessors
        return self.m1

    def set_m1(self,val):#mutators
        self.m1=val

    @classmethod#Decorartors
    def getSchool(cls):
        return cls.school

    @staticmethod
    def stat():
        print("This is a static method")
        return  0

s1=Student(12,12,33)
s2=Student(21,34,56)

print(s1.avg())
print(s2.avg())

print(s1.get_m1())
s1.set_m1(21)
print(s1.get_m1())

print(Student.getSchool())

print(Student.stat())#prints text and reurn 0 which is again printed
Student.stat()