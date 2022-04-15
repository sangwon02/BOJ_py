n = int(input())
cnt = n
for i in range(n):
    for i in range(n-cnt):
        print(" ",end="")
    for j in range(cnt):
        print("*",end="")
    cnt -= 1
    print("")