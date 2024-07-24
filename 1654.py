import sys
input = sys.stdin.readline

k, n = map(int, input().split())  # k와 n을 입력 받음
lanline = [int(input()) for _ in range(k)]  # 가지고 있는 랜선 k개 입력 받음
start, end = 1, max(lanline)  # start값과 end값 초기 설정

while start <= end:  # end가 start보다 작을 때 까지 계속
    mid = (start + end) // 2  # 중간 값을 찾고
    lines = 0  
    for i in lanline:  # 가지고 있는 랜선을 모두 꺼내서
        lines += i // mid  # 만들 수 있는 랜선의 수 찾음
    if lines >= n: # 만약 만들 수 있는 랜선의 수가 n보다 많거나 같으면
        start = mid + 1  # start값을 mid+1값으로 바꾸어줌
    else:  # 만들 수 있는 랜선의 수가 n보다 적으면
        end = mid - 1  # end값을 mid-1값으로 바꾸어줌
        
print(end)  # 답 출력