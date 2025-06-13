import sys
input = sys.stdin.readline

n = int(input())
nli = set(map(int, input().split()))  
# 리스트 보다는 set(집합)를 사용해 탐색시간 단축
m = int(input())
mli = list(map(int, input().split()))  
# m의 대한 수들은 그냥 리스트에 저장

for i in mli:  # mli에 있는 수들을 돌면서
    if i in nli:  # 만약 nli에 있다면
        print(1)  # 1을 출력해주고
    else:  # 아니면
        print(0)  # 0을 출력