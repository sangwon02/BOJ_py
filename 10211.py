import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    sum = [0]  # 누적합 구해서 저장할 리스트
    res = -10**10 # 답을 구할 변수
    for i in li:
        sum.append(sum[-1] + i)  # 누적합 계산
        
    # print("누적합 리스트", sum)  # 누적합 리스트 출력
    for i in range(n):
        for j in range(i+1, n+1):
            # 구간 합 계산 후 최소값 갱신
            # print("탑삭하는 인덱스 i", i, 탐색하는 인덱스 j", j, "합",sum[j] - sum[i])  # 구간 합 출력
            res = max(res, sum[j] - sum[i])
    print(res) # 최대값 출력