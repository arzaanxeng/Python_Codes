arr = [2,4,7,21,32,28,54,34,52,76,64,44]
target = 21
l=0
r= len(arr) - 1
while l <= r:
    m = l + (r - l) // 2
    if arr[m] == target:
        print("found!")
        break
    elif arr[m] > target:
        r = m - 1
    else:
        l = m + 1

