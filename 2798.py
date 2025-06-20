import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

sum = 0
res = 0  # 정답을 담을 변수

for i in range(n-2):  # 모든 경우의 수 구하고
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = li[i] + li[j] + li[k]  # 3카드의 합을 저장
            if m == sum: # 만약 모든 경우의 수 구하다가 m과 같은 값이 나오면
                print(sum)  # 출력 후
                exit()  # 파일 실행 종료
            elif m-sum > 0 and m-sum < m-res:  # sum이 m보다 작고 만약 res보다 m에 가깝다면
                res = sum  # res값을 sum값으로 갱신
print(res)