import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
stnum = int(input())

for i in range(stnum):  # 학생 수 만큼 반복
    n1, n2 = map(int, input().split())
    cnt = 0
    if n1 == 1:  # 남자라면
        for j in range(n2, n+1 ,n2): # 배수의 스위치를 바꾸어줌
            if li[j-1] == 1:
                li[j-1] = 0
            elif li[j-1] == 0:
                li[j-1] = 1
    else:  # 여자라면 
        while li[(n2-1)-cnt] == li[(n2-1)+cnt]:  # 좌우대칭이면
            if li[(n2-1)-cnt] == 0:  # 스위치를 둘 다 바꾸어줌
                li[(n2-1)-cnt] = 1
                li[(n2-1)+cnt] = 1
            elif li[(n2-1)-cnt] == 1:
                li[(n2-1)-cnt] = 0
                li[(n2-1)+cnt] = 0
            cnt += 1
            if ((n2-1)-cnt < 0) or (n2+cnt > len(li)):  # 인덱스의 값을 넘어갈때
                break  # 종료

# 답 출력
for i in range(1, n+1):
    print(li[i-1], end = " ")
    if i % 20 == 0 :
        print()
