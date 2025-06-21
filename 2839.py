import sys
input = sys.stdin.readline

# 내가 푼 풀이
n = int(input())  # 배달해야하는 설탕의 무게

num = 0 # 봉지의 개수
res = 0 # 봉지에 따른 설탕의 무게

while (n-res) > 2:  # 만약 남은 설탕의 무게가 2 이하면 종료
    # 남은 설탕이 15 미만이면서 3으로 나누어 떨어지는 경우
    if ((n - res) < 15) and ((n-res)%3 == 0): 
        num += ((n - res) // 3)  # 3kg필요한 만큼 사용
        res += n - res  # 남은 설탕의 무게를 res에 다 더해줌
        
    elif (n - res) >= 5:  # 만약 5키로를 담을 수 있다면
        num += 1  # 봉지의 개수 +1
        res += 5  # 봉지에 담은 설탕의 무게 +5
        
    elif (n - res) >= 3:  # 이때는 3킬로 담을 수 있는 경우
        num += 1
        res += 3
        
if res==n:  # 만약 남김없이 담았다면
    print(num)  # 사용한 봉지의 개수 출력
else:  # 남은 설탕이 있다면
    print(-1)  # -1 출력
    
# 다른 풀이!
n = int(input())

num = 0
while n >= 0 :
    if n % 5 == 0 :  # 5의 배수이면
        num += (n // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(num)
        break
    n -= 3  
    num += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)