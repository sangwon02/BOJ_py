import sys
input = sys.stdin.readline

def all_permutations():  # 모든 순열을 구해주는 함수 선언
    if len(ans) == n:  # 리스트의 길이가 n이 되면 값을 출력
        print(*ans)
        return  # return해줌
    else:
        for i in range(1, n+1):
            if i not in ans:  # 만약 ans에 들어가 있지 않다면
                ans.append(i)  # ans에 추가해주고
                all_permutations()  # 재귀함수 다시 실행
                ans.pop()  # 탐색이 끝나면 다시 값을 빼줌
    
n = int(input())
ans = []
all_permutations()