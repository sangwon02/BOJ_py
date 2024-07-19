import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]

# 치킨집과 집의 좌표 저장
homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if city_map[i][j] == 1:  # 집의 좌표 저장
            homes.append((i, j))
        elif city_map[i][j] == 2:  # 치킨집의 좌표 저장
            chickens.append((i, j))

# 가능한 치킨집 조합들 생성
chicken_combinations = list(combinations(chickens, m))

# m개를 뽑은 치킨집들의 치킨거리를 구해주는 함수
def calculate_distance(homes, chickens):
    total_distance = 0
    for home in homes:
        current_distence = float('inf')
        for chicken in chickens:  # 치킨집들의 좌표를 돌면서
            # 집과의 거리 구하고
            distance = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            current_distence = min(current_distence, distance) 
        total_distance += current_distence  # 최솟값 들로 구한 거리들을 저장하고  
    return total_distance  # 리턴

# 모든 치킨집 조합에 대해 치킨 거리 계산
result = float('inf')  # 정답을 저장할 변수
for combi in chicken_combinations:
    # m개의 치킨집들을 뽑은 것 들을 토대로 치킨 거리가 작은 값을 저장
    current_distance = calculate_distance(homes, combi) 
    result = min(result, current_distance)

# 가장 낮은 치킨 거리 출력
print(result)