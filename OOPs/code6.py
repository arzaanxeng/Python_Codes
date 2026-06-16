# Calculator using Magic methods

class Calculator:

    def __init__(self , num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self):
        return self.num1 + self.num2

    def __sub__(self):
        return self.num1 - self.num2

    def __mul__(self):
        return self.num1 * self.num2

    def __truediv__(self):
        return self.num1 / self.num2

    def __floordiv__(self):
        return self.num1 // self.num2

    def __mod__(self):
        return self.num1 % self.num2

operation = Calculator(3 , 8)
print(f"The sum of two numbers is : {operation.__add__()}")
print(f"The product of two numbers is : {operation.__mul__()}")
print(f"The division of two numbers is : {operation.__truediv__()}")


