
# UNDERSTANDING *args (Arbitrary Positional Arguments)
# =========================================================================
"""
The * operator packing mechanism tells Python: "Take all individual positional
arguments passed into this function and pack them together into a single TUPLE."
You can name it anything (e.g., *numbers), but *args is the standard convention.
"""

def add(*args):
    # Inside the function, 'args' is treated as a regular tuple: (10, 20, 45, 65, 75)
    # The built-in sum() function can easily iterate over a tuple to add them up.
    return sum(args)


def mul(*args):
    # Inside the function, 'args' is a tuple: (3, 8, 9, 2, 7)
    result = 1
    for i in args:
        result *= i
    return result

# =========================================================================
# UNDERSTANDING **kwargs (Arbitrary Keyword Arguments)
# =========================================================================
# The ** operator packing mechanism tells Python: "Take all named/keyword
# arguments (key=value) and pack them together into a single DICTIONARY."
# Like args, you can name it anything, but **kwargs is the standard convention.

def fun(**kwargs):
    # Inside the function, 'kwargs' is treated as a regular dictionary:
    # {'a': 1, 'b': 2, 'c': 3}

    # We use .items() to cleanly extract both the key (k) and the value (val)
    for k, val in kwargs.items():
        print(k, " = ", val)


# =========================================================================
# CODE EXECUTION & DEMONSTRATION
# =========================================================================

# 1. Testing **kwargs
# We pass named key-value pairs. Python packs them into a dictionary for 'fun'.
fun(a=1, b=2, c=3)

print("---")  # Visual separator for output

# 2. Testing *args with addition
# We pass 5 separate positional numbers. Python packs them into a 5-element tuple.
print(add(10, 20, 45, 65, 75))

# 3. Testing *args with multiplication
# We pass 5 separate positional numbers. Python packs them into a 5-element tuple.
print(mul(3, 8, 9, 2, 7))