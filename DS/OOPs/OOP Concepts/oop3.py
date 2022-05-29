"""
types of variables
variables are three types
1) class->common to all objcts
2) instance -> different for each object
"""
class Car:
    #Class variables
    wheels=4#common to all objects
    def __init__(self):
        #instance Variables
        self.mil=10
        self.com="BMW"

c1=Car()
c2=Car()

#c1.mil=21

print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)
print(Car.wheels)
#print(Car.mil) #enrror
