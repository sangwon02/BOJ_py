import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pascal = []  # 파스칼의 삼각형 생성

for i in range(n):
    li = []  # i번째행에 추가할 리스트를 호출
    for j in range(0, i+1):
        if j == 0 or j == i:  # 추가해야되는 곳이 양 끝 쪽이면 
            li.append(1)  # 1을 추가
        else:  # 양 끝 쪽이 아니면
            li.append(pascal[i-1][j-1]+pascal[i-1][j]) # 위 행에 인접한 두수를 더해서 추가
    
    pascal.append(li)  # pascal리스트에 추가해준다.
    
print(pascal[-1][m-1]) # 답 출력