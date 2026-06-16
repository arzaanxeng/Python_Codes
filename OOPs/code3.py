# multiple inheritance
class Human:
    def __init__(self, name):
        self.name = name

class Ability:
    def __init__(self , id):
        self.id = id

class Robot(Human , Ability):
    def __init__(self, name , id):
        Human.__init__(self , name)
        Ability.__init__(self , id)

obj1 = Robot("Robot1", 1)




