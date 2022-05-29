"""
    inner class in python
    object of inner class should be inside of outer classi.e., line 10
"""

class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()##creation of object of inner class inside the outer class(1)

    def show(self):#mtd of student
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.ram="16gb"
            self.cpu="i3"
            self.disk="1TB"

        def show(self):#mtd of laptop
            print (self.ram,self.cpu,self.disk)

s1=Student("Balaji",23)
s2=Student("MSC",25)
s1.show()

# s1.lap.show()# anothe rway of accesing the attributes
# print(s2.lap.disk)

"""
    lap1=Student.Laptop()   To create object diresctly oustide (2)
    lap1.disk
    lap1.show() 
"""

"""
    print(s1.name)
    print(s2.name) This wont lok good instead s1.show( need to print all details about student
    
    s1.show()
    print(s1.lap.ram) #16gb one way of accessing inner class attributes
"""
"""
    To create two another different objects
    
    lap1=s1.lap
    lap2=s2.lap
    print(lap1.disk)#1TB
    lap2.show()#16gb i3 1TB
"""

