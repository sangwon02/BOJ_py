import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = []  # 동전을 담을 리스트

for _ in range(n):
    li.append(int(input()))

li.reverse() # 오름 차순이 아닌 내림차순으로 정렬
cnt = 0 # 리스트에 있는 동전을 체크할 변수
res = 0 # k를 만들기 위해 필요한 코인의 수

while k != 0:
    # 큰 코인부터 
    if k >= li[cnt]: # 현재 탐색중인 코인의 값어치가 남은 돈 이상이면
        res += k//li[cnt]  # 사용한 코인의 수만큼 +
        k = k%li[cnt]  # 남은 돈을 나누기한 나머지로 업데이트 해주고
        
    else:  # 아니면
        cnt += 1  # 다음 코인탐색
        
print(res) # 답출력