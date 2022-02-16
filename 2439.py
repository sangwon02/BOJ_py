x = int(input())

for n in range(1,x+1,1):
    for j in range(x,n,-1):
        print(" ", end='')
    for i in range(n):
        print("*", end='')
    print("")