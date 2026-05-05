"""
1.The "Unique Path" Navigator:
Concept: Sets, List Comprehensions, and Logic.
The Challenge: Write a function that takes a list of coordinates (tuples) representing a robot's path.
Some coordinates might be visited multiple times. Your goal is to return a list of only the first five
unique locations visited, in the order they were first encountered. If there are fewer than five, return
all of them.
"""

path = [(0, 0), (1, 0), (0, 0), (2, 1), (1, 0), (3, 3), (4, 4), (5, 5), (0, 0) , (7,0) , (4,3)]

def unique_locations(path):
    unique_path = []
    for i in path:
        if i not in unique_path:
            unique_path.append(i)
            if len(unique_path) == 5:
                break
    return unique_path

# Searching a list takes O(n) time because Python has to look at every element one by one.
# Using a set for tracking "seen" items takes O(1) time (instant lookup).

def get_first_five_unique(path):
    unique_list = []
    seen = set()  # Using a set for high-speed lookups

    for coord in path:
        if coord not in seen:
            unique_list.append(coord)
            seen.add(coord)

            if len(unique_list) == 5:
                break

    return unique_list

result = get_first_five_unique(path)
print(f"The set of first five unique paths taken were :  {result}")
print(f"The set of first five unique paths taken were :  {unique_locations(path)}")









