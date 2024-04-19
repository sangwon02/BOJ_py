import sys
input = sys.stdin.readline

t = int(input()) 

for i in range(t):  # t번 반복
    n = int(input())  # 하루에 배달되는 사료의 양 입력 받음
    feed = []  # 사료양 받을 리스트
    feed = list(map(int, input().split()))  # 사료양을 입력 받음
    cnt = 1
    nextday = []  # 다음 날 줘야 할 사료양 계산
    
    while sum(feed) <= n:  # 줘야 할 사료양 보다 적으면 계속 반복
        nextday.append(feed[0]+feed[1]+feed[2]+feed[4])  # 돼지들이 다음날 원하는 
        nextday.append(feed[1]+feed[2]+feed[3]+feed[5])  # 사료양을 업데이트 해줌
        nextday.append(feed[2]+feed[3]+feed[4]+feed[0])
        nextday.append(feed[3]+feed[4]+feed[5]+feed[1])
        nextday.append(feed[4]+feed[5]+feed[0]+feed[2])
        nextday.append(feed[5]+feed[0]+feed[1]+feed[3])
        cnt += 1  # 줄 수 있는 날짜 +1
        feed = nextday 
        nextday = []  # 다음날 줘야 할 사료양 비워줘 다음에 또 사용
                
    print(cnt)  # 몇일 줄 수 있는지 출력