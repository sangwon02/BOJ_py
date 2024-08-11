from collections import deque
import sys
input = sys.stdin.readline

n=int(input()) # 컴퓨터의 수
v=int(input()) # 컴퓨터쌍의 수

graph = [[] for i in range(n+1)]
visited=[0]*(n+1) # 방문 여부 확인

for i in range(v):  # 연결된 그래프 생성
    a,b=map(int,input().split())  # 연결된 컴퓨터의 쌍 입력 받음
    graph[a]+=[b]  # a와 b연결
    graph[b]+=[a] 

visited[1]=1  # 1번 컴퓨터 방문

Q=deque([1])

while Q:  # 방문한 컴퓨터들의 여부 확인
    c=Q.popleft() 
    for nx in graph[c]:
        if visited[nx]==0:  # 만약 아직 방문되지 않은 컴퓨터면
            Q.append(nx)  
            visited[nx]=1  # 방문해줌

print(sum(visited)-1)  # 방문 표시된 컴퓨터의 수 출력