"""
Practice
"""
class Dog:

    def __init__(self,name,level):
        self.name=name
        self.level=level
        self.dogPet=self.Pet()

    def eat(self):
        print(self.name,self.level)
        self.dogPet.info()

    class Pet:
        def __init__(self):
            self.type="P-kid"
            self.age="P-younger"
        def info(self):
            print(self.type,self.age)

"""
    #1
    o1=Dog.Pet()
    print(o1.age,o1.type,sep=",")
    o1.info()
"""
"""
    #2
    o2=Dog("MIckey","Mother")
    o2.dogPet.info()
"""

o3=Dog("jimmy","Kid")
o3.eat()
o3.dogPet.info()
