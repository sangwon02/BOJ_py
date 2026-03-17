import sys
input = sys.stdin.readline

n = int(input())

li = [""] * (n+1) # n 크기의 리스트 생성

if n == 1:
    print(0)
    exit()
elif n == 2:
    print(1)
    exit()
elif n == 3:
    print(1)
    exit()
else:
    # 일단 1은 0으로 초기화
    li[1] = 0
    # 2, 3은 1로 초기화
    li[2] = 1
    li[3] = 1
    
    # 4부터 n까지의 수에 대해서 li에 저장
    for i in range(4, n + 1):
        li[i] = li[i-1] + 1 # 1을 빼는 경우를 일단 넣어둠
        
        if i%3 == 0:  # 3으로 나누어 떨어지는 경우
            li[i] = min(li[i], li[i//3]+1)  # 1을 빼는 경우와 3으로 나누는 경우 중 작은 값으로 업데이트
            
        if i%2 == 0: # 2로 나누어 떨어지는 경우
            li[i] = min(li[i], li[i//2]+1) # 1을 빼는 경우와 2로 나누는 경우 중 작은 값으로 업데이트
    print(li[n])