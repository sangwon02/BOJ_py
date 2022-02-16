#소수 구하는 프로그램

n = int(input())
i = 2
while n != 1:
    if n % i == 0:
        print(i)
        n = n//i
    else:
        i+=1