import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

start = 1  # 시작점
end = 1000000 * m # 마지막점
result = 1 # 정답답
while start <= end:
    middle = (start + end) // 2 # 중간 시간 값을 통해
    balloon = 0
    for i in li:
        balloon += middle // i  # 만들 수 있는 풍선의 수를 구하고
    
    if balloon < m:  # 풍선의 수가 m(원하는 값)보다 작으면
        start = middle + 1 # 시작 값을 중간값의 +1 값으로 바꿔주고
    else:  # 만약 m보다 크면
        result = middle  # 정답 값 변경
        end = middle - 1 # 마지막점을 중간 값으로 변경
    
print(result)