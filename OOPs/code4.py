# method overwriting

class Robot:
    def talk(self):
        print("I can't talk")

class Human(Robot):
    def talk(self):
        #super().talk() --> this could access the method within the parent class
        print("I can talk")

obj1 = Human()
obj1.talk()

""" 
Here we can see that the method which was called in this is the one within the main class
and the method within the Parent class is not called due to over riding but it can be accessed with
the help of super() method and it would be able to access the method within the parent class.
"""
obj2 = Robot()
obj2.talk()
