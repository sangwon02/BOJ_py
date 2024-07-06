import sys
import math
input = sys.stdin.readline

n, k, l = map(int, input().split())  # 각 선수 수와 지민, 한수의 번호 입력 받음
cnt = 1  # 몇 라운드인지 카운트 해줄 변수
while True:
    # 라운드가 지날때 마다 자기번호/2 해준 후 올림했을때
    k = math.ceil(k/2)  # 같은 번호 끼리 만남
    l = math.ceil(l/2)
    if k == l:  # 만약 지민이와 한수가 만나면 몇 라운드에 만났는지 출력
        print(cnt)
        break
    cnt += 1  #만나지 않았다면 다음 라운드로 이동
