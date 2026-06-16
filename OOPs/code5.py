# Abstraction

from abc import ABC, abstractmethod
class Franchise(ABC):
    @abstractmethod
    def intro(self):
        pass

"""
This is done in order to make sure that if a company wants to ensure that each class in the
program must contain a particular type of method than we use abstraction.
"""
class Feature_1(Franchise):
    def intro(self): # This must be defined within this class
        pass
    def f1(self):    # This method is specific to this class only !
        print("I am f1")

class Feature_2(Franchise):
    def intro(self):  # This must be defined within this class
        pass
    def f2(self):     # This method is specific to this class only !
        print("I am f2")

class Feature_3(Franchise):
    def intro(self):  # This must be defined within this class
        pass
    def f3(self):     # This method is specific to this class only !
        print("I am f3")

obj1 = Feature_1()
obj2 = Feature_2()
obj3 = Feature_3()
