n = int(input())
arr = map(int, input().split())
num1 = 0
for j in arr:
    no = 0
    if j > 1 :
        for i in range(2, j):  
            if j % i == 0:
                no += 1  
        if no == 0:
            num1 += 1  
print(num1)