# -------------------------------------------------------------------------
# CLASS DEFINITION
# A class acts as a blueprint or template for creating objects.
# -------------------------------------------------------------------------
class Car:
    # CLASS ATTRIBUTE / VARIABLE
    # This variable belongs to the class itself, not to any specific object.
    # Every object created from this class shares this exact same variable.
    car_number = 25

    # ---------------------------------------------------------------------
    # CONSTRUCTOR (__init__ Method)
    # Automatically runs whenever you create a new object (e.g., Car(...)).
    # 'self' represents the specific object being created right now.
    # ---------------------------------------------------------------------
    def __init__(self, name, color, model, cost):
        # INSTANCE ATTRIBUTES / VARIABLES
        # These are unique to each individual object.
        # Using 'self.' attaches the incoming data to the specific object.
        self.name = name  # Name of this specific car
        self.color = color  # Color of this specific car
        self.model = model  # Model of this specific car
        self.cost = cost  # Cost of this specific car

    # ---------------------------------------------------------------------
    # INSTANCE METHOD
    # This method belongs to the individual objects created from the class.
    # It must take 'self' as its first argument to access the object's unique data.
    # ---------------------------------------------------------------------
    def details(self):
        # Uses 'self.' to pull up the specific attributes of whichever car called it
        print(f"The car is {self.name}, model {self.model} of {self.color} color rated at price {self.cost}")

    # ---------------------------------------------------------------------
    # CLASS METHOD (@classmethod)
    # This method is bound to the Class, not its individual objects.
    # Instead of 'self', its first argument is 'cls', which refers to the Class itself.
    # Great for actions that involve class-wide variables (like 'car_number').
    # ---------------------------------------------------------------------
    @classmethod
    def intro(cls):
        print("Hello, Sir/Ma'am what would you like to see?")

    @classmethod
    def car_numbers(cls):
        # Uses 'cls.' to access the class attribute 'car_number'
        print(f"The number of cars in the showroom is {cls.car_number}")

    # ---------------------------------------------------------------------
    # STATIC METHOD (@staticmethod)
    # A completely independent function bundled inside the class for organization.
    # It does NOT take 'self' or 'cls' as a mandatory first parameter.
    # It cannot modify object state or class state; it just does a standalone job.
    # ---------------------------------------------------------------------
    @staticmethod
    def car_design(car):
        # This parameter 'car' is just a normal argument, not a special OOP keyword
        print("The car is an SUV")


# CODE EXECUTION (Using the Class)

# 1. Calling a Class Method
# You don't need to create an object to call a class method; call it directly using the Class name.
Car.intro()

# 2. Creating an Object (Instantiation)
# This allocates memory and fires up the __init__ constructor, passing the arguments to 'self'.
obj1 = Car(name="AUDI", color="red", model="Q7", cost=400000)

print(obj1.car_number)
# 3. Calling an Instance Method
# Since 'obj1' calls it, Python automatically passes 'obj1' into the 'self' parameter behind the scenes.
obj1.details()