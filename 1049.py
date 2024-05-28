import sys
input = sys.stdin.readline

n, m = map(int, input().split())

share = n//6  # 패키지로 살 수 있는 몫을 구하고
rest = n%6  # 패키지로 샀을 때 남는 키타줄에 갯수
result = 0
packages = []
individuals = []

for i in range(m):  
    n1, n2 = map(int, input().split())
    packages.append(n1)  # 모든 패키지의 값을 저장
    individuals.append(n2)  # 모든 낱개의 값을 저장
    
packages_min = min(packages)  # 패키지 값 중에 가장 낮은 값을 저장
individuals_min = min(individuals)  # 낱개의 값 중에 가장 낮은 값을 저장

# 일단 가장 낮은 패키지 값과 몫을 곱한 값과 가장 낮은 낱개의 값에 나머지를 곱한 값을 저장
result = packages_min*share + individuals_min*rest  

# 가장 낮은 패키지 값과 (몫+1)을 곱한 값이 더 작다면
if packages_min*(share+1) < result:
    result = packages_min*(share+1)  # 그 값을 저장
    
# 가장 낮은 낱개의 값에 필요한 기타줄을 곱한 값이 더 작다면
if individuals_min*n < result:
    result = individuals_min*n  # 그 값을 저장
    
print(result)