from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
heapq = []

for _ in range(n):
    num = int(input())
    if num != 0:   # 0이 아닌 정수이면
        heappush(heapq, (abs(num), num))  
        # 삽입을 하는데 절댓값을 기준으로 인덱스를 두고 삽입을 한다! (리스트를 넣으면 된다(x,y)에서 x를 기준으로)
        print("현재 배열 상태", heapq)
    elif num == 0:  
        if heapq:  # 비어있지 않으면
            print(heappop(heapq)[1]) # (x,y)에서 y(절댓값이 아닌 값)의 값을 출력한다.
            print("현재 배열 상태", heapq)
        else:  
            print(0)
        