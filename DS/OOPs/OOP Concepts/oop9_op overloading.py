"""
Operator Overloading

a=2
b=1
print(int.__add__(a,b))
#overloading + operator
#overloading > operator

"""
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        t1=self.m1+other.m1
        t2=self.m2+other.m2
        s3=Student(t1,t2)
        return s3

    def __gt__(self, other):
        if (self.m1+self.m2)>(other.m1+other.m2):
            return True
        else:
            return  False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
        #return '%d %d'%(self.m1,self.m2)

mark=Student(21,19)
mark2=Student(13,12)

tot=mark+mark2  #overloading + operator
print(tot.m2)

if mark>mark2:  #overloading > operator
    print("student 1 wins")
else:
    print("student 2 wins")

#print(mark) #printing address

print(mark2)#overloading __str__() mtd which is print method






