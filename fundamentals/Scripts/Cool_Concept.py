# Working with tuple non mutability
t = (1,2,3,4,[5,6])
print(f"The tuple is : {t}\nThe address is : {id(t)}\n")

t = list(t)
t.append(7)
t = tuple(t)
print(f"The tuple is : {t}\nThe address is : {id(t)}\n")

"""Even though the tuple is non mutable but still due to the fact that list is mutable ,
   we can see a very unique behaviour"""
t[4].append(7)
print(f"The tuple is : {t}\nThe address is : {id(t)}\n")

a = 256
b = 256
print(b is a)
# Due to python caching this will be true as the value of integer being in between [-5 , 256] it will point to the same address!

q = 1000
w = 1000
print(w is q)
# Due to python caching failiure this will be false as the value of integer does not lie in between [-5 , 256] it will not point to the same address!