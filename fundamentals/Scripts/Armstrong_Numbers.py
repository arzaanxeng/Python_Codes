n = int(input("Enter the required number : "))
original_n = n
# Calculating the number of digits in the input
digits = 0

while n>0:
    digits = digits + 1
    n = n//10

original_n_ = original_n

arm_num = 0
while original_n > 0:
    rem = original_n%10
    arm_num = pow(rem , digits) + arm_num
    original_n = original_n//10

if original_n_ == arm_num:print(f"The number {original_n_} is an Armstrong Number")
else : print(f"The number {original_n_} is not an Armstrong Number")