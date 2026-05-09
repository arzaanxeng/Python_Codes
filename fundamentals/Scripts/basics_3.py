l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
# is keyword would actually match the id's of both of them --> False
print(l1 is l2)
# == would match the values inside the list --> True
print(l1 == l2)

t = (1,2,3,[4,5])
print(id(t))
t[3].append(6)
# Even though the tuple is un-mutable but the list is mutable so the elements inside the tuple got mutated
print(id(t))
print(t)



