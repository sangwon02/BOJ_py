import sys
input = sys.stdin.readline

list = []
n = 400  # n의 제한이 10000까지이니 소수인 수를 400까지 list에 넣음 
for i in range(2, n+1):
    list.append(i)
for i in range(2, n+1):
    for j in range(2, n+1):
        s = i*j
        if s > n:
            break
        if s in list:
            list.remove(s)

n = int(input())  # 숫자를 입력 받고
i = 0

while True:  # 무한반복
    if n < 6:  # n이 6보다 작으면
        print(6)  # 연속한 소수를 곱한 값중에 가장 작은 값인 6 출력
        break  # 무한 반복 종료
    if (list[i]*list[i+1]) <= n and (list[i+1]*list[i+2]) > n :  # 리스트를 이용해 범위를 찾아
        print(list[i+1]*list[i+2])  # 원하는 값 출력
        break # 종료
    else:  # 원하는 범위에 있지 않다면
        i += 1  # i에 +1
    if i == 399:  # 만약 i가 399 되면 
        break  # 종료

