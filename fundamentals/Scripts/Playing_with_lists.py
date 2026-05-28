# Finding the minimum value element in the list
l = [1,2,3,4,-3,9,0,56,90,76]
minimum = l[0]
for i in range(len(l)):
    if l[i] < minimum:
        minimum = l[i]
print(f"The minimum element element in the list is : {minimum}\n")

# Finding the maximum value element in the list
l = [1,2,3,4,-3,9,0,56,90,76]
maximum = l[0]
for i in range(len(l)):
    if l[i] > maximum:
        maximum = l[i]
print(f"The maximum element in the list is : {maximum}\n")

# Finding the second_highest value element
l = [1,2,3,4,-3,9,0,56,90,76]
l.sort( reverse = True)
print(f"The second largest element in the list is :{l[1]}\n")

# Updating the list with no repeating values
l_unique = []
for i in range(len(l)):
    if l[i] not in l_unique:
        l_unique.append(l[i])
print(f"The unique element list is : {l_unique}\n")

