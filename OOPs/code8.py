# lambda , map , filter , zip

def is_even_odd(num):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

is_even_odd(10)

# Let's make this code precise using lambda fxn
is_even_odd = lambda x : print(x, "is an even number") if x % 2 == 0 else print(x, "is an odd number")
is_even_odd(17)

l = ["Arzaan","Sam","Jennifer","Obama"]
a = list(map(len , l))
print(a)
joint_list = list(zip(l,a))
print(joint_list)

temp_c = [12,34,24,31,19]

temp_f = list(map(lambda x : ((x*3/5) + 35) , temp_c))
print(temp_f)
