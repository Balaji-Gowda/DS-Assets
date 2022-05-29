"""
Duck Typing

Its not nede which class object is provided if it contains execute method then we can pass that object(class) as parameter
it is not concerned that whic clas object it is but only we need execute method in it

"""

class Pycharm:
    def execute(self):
        print("execution")
        print("Spell check")
        print("Color enhancement")

class Myeditor:
    def execute(self):
        print("execution")
        print("Spell check")
        print("Color enhancement")
        print("Also error detection")
        print("Error correction")

class Laptop:
    def code(self,ide):
        ide.execute()



ide=Myeditor()

lap=Laptop()
lap.code(ide)


