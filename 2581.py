n = int(input())
n1 = int(input())
num1 = 0
for j in range(n, n1+1, 1):
    no = 0
    if j > 1 :
        for i in range(2, j):  
            if j % i == 0:
                no += 1
        if no == 0:
            num1 += j
if num1 == 0:
    print(-1)
    exit()
print(num1)
for j1 in range(n, n1+1, 1):
    no1 = 0
    if j1 > 1 :
        for i1 in range(2, j1):  
            if j1 % i1 == 0:
                no1 += 1
        if no1 == 0:
            print(j1)
            break