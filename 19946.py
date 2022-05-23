N = int(input()) #정수를 받음
cnt = 64 #실수한 구간을 확인해줄 변수

while N % 2 == 0: #N이 2로 나누어지면 반복
    N //= 2 #N을 2로 나누어줌
    cnt -= 1 #cnt에 -1를 해줌

print(cnt) #실수한 구간 출력