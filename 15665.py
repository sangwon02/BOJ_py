import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []

def dfs():
    if len(result) == m: # 만약 result의 길이가 m이면
        print(*result) # result의 원소 출력 후
        return  # 리턴
    
    overlap = 0 # 중복된 수열 방지
    for i in range(n): 
        if overlap != nums[i]:  # overlap과 다르다면
            result.append(nums[i])  # result에 추가해주고
            overlap = nums[i]  # overlap 갱신
            dfs()  # 다음 원소 추가하기 위해 dfs호출
            result.pop()  

dfs()