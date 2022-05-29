"""
The __init__ method
"""

class Computer:
    #attributes-> variables
    #behaviour-> methods
    def __init__(self,cpu,ram):
        #need to assign values to objects
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print(self.cpu,self.ram)

com1=Computer("i5",16)
com2=Computer("Ryzen-3",8)
"""
Computer.config(com1)
Computer.config(com2)"""
com1.config()
com2.config()