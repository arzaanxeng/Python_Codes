import numpy as np
import time
a = [i for i in range(10000000)]
b = [i for i in range(10000000)]

c =[]
start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])
end = time.time()
t1 = end - start
print(f"The time required for the code of list to run is : {t1}")

a = np.arange(10000000)
b = np.arange(10000000)
start_2 = time.time()
c = a + b
end_2 = time.time()
t2 = end_2 - start_2
print(f"The time required for the code of numpy to run is : {t2}")
ratio = t1/t2
print(f"The code of numpy ran {ratio} times faster than code of list")