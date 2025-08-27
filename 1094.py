import sys
input = sys.stdin.readline

x = int(input())

# 가지고 있는 막대기의 길이를 큰 순서대로 리스트에 저장
sticks = [64, 32, 16, 8, 4, 2, 1]

cnt = 0 # 사용된 막대기의 개수

for i in range(len(sticks)):
    # 목표 길이(x)가 현재 확인하는 막대기의 길이보다 크거나 같다면
    if x >= sticks[i]:
        cnt += 1 # 사용된 막대기의 개수(cnt)를 1 증가시
        x -= sticks[i] # 목표 길이(x)에서 사용한 막대기의 길이만큼 빼줌

    if x == 0:
        break

# 사용된 막대기의 총 개수 출력
print(cnt)