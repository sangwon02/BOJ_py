import heapq  # heapq 모듈 불러옴
import sys
input = sys.stdin.readline

heap = []  # 힙 역할을 할 빈 리스트 생성

n = int(input())

for i in range(n):  
    num = int(input())  # 정수를 입력 받고
    if num == 0:  # 만약 0을 입력 받았다면
        if len(heap)>0:  # 힙이 비어있지 않다면
            print(heapq.heappop(heap))  
            # pop(가장 낮은 수 제거)해주고 그 값을 출력
        else: # 비어있다면 0 출력
            print(0)
    else:  # 0이 아닌 다른 자연수가 들어왔다면 추가해줌(최소힙 기준으로)
        heapq.heappush(heap, num)