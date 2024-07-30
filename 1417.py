import sys
input = sys.stdin.readline

n = int(input())
one = int(input())  # 기호 1번의 득표수를 따로 저장해둠
li = []

for _ in range(n - 1):  # 기호 1번을 제외한 나머지 후보들의 득표 수 입력 받음
    li.append(int(input()))

li.sort(reverse=True)  # 내림차순으로 정리

cnt = 0  # 매수한 사람의 수
if n == 1:  # 만약 기호 1번만 있다면
    print(0)  # 바꿀 필요 없음
else:
    # 다른 득표자 중 가장 많은 득표 수가 1번보다 많다면 계속 실행
    while li[0] >= one:  
        one += 1 # 기호 1번의 득표수로 변경
        li[0] -= 1  # 다른 득표자는 -1 해줌
        cnt += 1  # 매수한 사람의 수 +1
        # 다시 한번 내림차순으로 정렬 해주어 맨앞에 최다 득표자가 있도록 해줌
        li.sort(reverse=True)  
    print(cnt)