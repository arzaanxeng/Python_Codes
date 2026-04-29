"""
List Manipulation: Remove duplicates from a list or find the 2nd largest number.
Dictionary Tasks: Merge two dictionaries and count the frequency of each character in a string
"""
# A list with multiple repeated values
l = [1,2,3,4,5,6,7,8,9,2,3,4,5]
l_new = []
for item in l :
    if item not in l_new:
        l_new.append(item)

l_new.sort(reverse = True)
print("=*"*35)
print(f"The second largest number in the list is : {l_new[1]}\n")

# Merging two dictionaries
print("=*"*35)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(dict1)
print(dict2)
merged = dict1 | dict2
print(f"The merged dictionary is : {merged}\n")

# Counting the frequency of each character in a string
try:
    print("=*" * 35)
    string = input("Enter a string: ")
    roster = dict()
    for item in string:
        if item not in roster.keys():
            roster[item] = 1
        else:
            roster[item] += 1

except ValueError:
    print("Invalid input")

import pprint
pprint.pprint(roster)





