# from abc import ABC, abstractmethod


# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass

#     def cls(self):
#         print("Hello")


# class mouse(Computer):
#     def work(self):
#         print("moving cursor")

#     def process(self):
#         print("hi")


# mou = mouse()

# mou.work()

def convert_upper(f):
    print("convert_upper")

    def wrap(*args, **kwargs):
        print("wrap")
        x = f(*args, **kwargs)
        return x.upper()
    return wrap


@convert_upper
def my_name(name):
    print("my_name")
    return name
