class BagFactory:

    def __init__(self, name, chains, zips):
        self.name = name  # Name of this specific car
        self.chains = chains  # Color of this specific car
        self.zips = zips  # Model of this specific car

    def details(self):
        print(f"The name is {self.name}")
        print(f"The number of chains is/are {self.chains}")
        print(f"The number of zips is/are {self.zips}")

class Reebok(BagFactory):
    def __init__(self, name, chains, zips , color):
        super().__init__(name , chains , zips)
        self.color = color

    def details(self):
        print(f"The color is {self.color}")
        return super().details()

class Campus(Reebok):
    def __init__(self, name, chains, zips , color,price):
        super().__init__(name, chains, zips , color)
        self.price = price

    def details(self):
        print(f"The price is {self.price}")
        return super().details()

obj1 = Campus("CampusX" , 5 , 3 , "red" , 1500)
obj1.details()




