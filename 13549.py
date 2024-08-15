import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
INF = 1000000000

def dijkstra(n,k):
    li = [INF]*(100001) # 리스트 100,000개로 생성
    li[n] = 0  # 현재 누나 위치 초기화
    hq = []
    heapq.heappush(hq,(0,n))
    
    while hq:
        w,n = heapq.heappop(hq)
        for nx in [(n+1,1),(n-1,1),(n*2,0)]:  # n+1, n-1, n*2를 했을때 지정된 범위를 넘지 않고
            if 0 <= nx[0] <= 100000 and li[nx[0]] > w + nx[1]:  # 만약 그전에 있던 값보다 작다면
                li[nx[0]] = w + nx[1]  # 값을 새로 업데이트 해준다.
                heapq.heappush(hq,(li[nx[0]],nx[0]))
    print(li[k])  # 최종 답 출력
dijkstra(n,k)