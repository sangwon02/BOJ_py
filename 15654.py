import sys
input = sys.stdin.readline

def dfs():  # 함수 선언
    if len(result) == m: # result의 길이가 m일때 출력 
        print(*result)
        return  # return을 해주어 함수를 종료 시킴
    else:
        for i in li:  # li에 넣은 값으로 탐색
            if i not in result:  # 만약 result에 들어있지 않다면
                # 자식노드로 이동
                result.append(i)
                dfs()
                result.pop()  # 답을 출력했다면 부모노드로 이동
    
n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=False)  #숫자, 문자 오름차순으로 정렬
result = []
dfs()

