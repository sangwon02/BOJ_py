import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))

nums = list(map(int, input().split()))

res = 0
# 첫 번째 도시의 기름값을 초기 최저가로 설정
min_price = nums[0]

for i in range(n - 1):
    # 현재 도시의 기름값이 이전에 저장된 최저가보다 싸면, 최저가를 갱신
    # 앞으로는 이 가격으로 주유하는 것이 이득
    if nums[i] < min_price:
        min_price = nums[i]
    
    # 다음 도시로 이동하기 위한 기름은, 현재까지 파악된 가장 저렴한 가격으로 주유
    res += min_price * roads[i]

print(res) # 답 출력