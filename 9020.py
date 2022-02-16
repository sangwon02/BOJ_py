#짝수를 입력하면 소수 더하기 소수를 구하는 프로그램

li = [False, False] + [True]*10002

for i in range(2, 10002):
    if li[i]:
        for j in range(2*i, 10002, i):
            li[j] = False

num = int(input())

for i in range(num):
    n = int(input())
    a = n//2
    b = a
    while a>0:
        if li[a] and li[b]:
            print(a, b)
            break
        else:
            a-=1
            b+=1