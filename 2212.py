import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# 센서 좌표를 정렬 (중복은 set으로 자동 제거 후 정렬)
sensors = sorted(list(set(map(int, input().split()))))

# N을 중복 제거 후의 센서 개수로 업데이트
# 만약 중복 제거 후 센서 수가 K 이하라면 비용은 0
n = len(sensors)
if k >= n:
    print(0)
    sys.exit()
    
# 인접한 센서들 사이의 모든 간격(거리)을 계산
distances = []
for i in range(1, n):
    distances.append(sensors[i] - sensors[i-1])

# 간격들을 오름차순으로 정렬
distances.sort()

result = sum(distances[:n - k])

print(result)
