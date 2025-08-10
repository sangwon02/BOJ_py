import sys
input=sys.stdin.readline

n=int(input())

arr=[0]
li = [0 for _ in range(n+1)]

for _ in range(n):
    arr.append(int(input()))


if n==1:
    print(arr[1])

else:
    li[1] = arr[1]
    li[2] = arr[1] + arr[2]

    #점화식 구현
    for k in range(3,n+1):
        li[k] = max(li[k-3] + arr[k-1], li[k-2]) + arr[k]

    print(li[n])