import sys
input = sys.stdin.readline

n = int(input())
cnt666 = 666  # 시작 숫자를 666부터 시작
cnt = 0  # 몇 번째로 작은 수인지 카운트

while True:
    if '666' in str(cnt666):  # 666이 숫자에 있다면 
        cnt += 1  # 카운트 +1
    if cnt == n:  # 만약 n과 같다면 n번째로 작은 666이 들어가는 숫자이므로
        print(cnt666)  # cnt666출력
        break  # whlie문 종료
    cnt666 += 1  #다음 확인 할 숫자로 넘어감