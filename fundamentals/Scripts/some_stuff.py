n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print("\n")
    for j in range(i):
        print("*",end="")

m = int(input("\nEnter the number of rows: "))
for i in range(1,m+1):
    print("\n")
    for j in range(m+1-i):
        print("*",end="")