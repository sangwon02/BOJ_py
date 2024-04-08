import sys
input = sys.stdin.readline

n = int(input())

totalcoin = 0
totalmoney = 0
remaining = n  # 앞으로 거슬러줘야 할 돈
while n != totalmoney:  # 거슬러 준돈이 n 일 때 종료
    if remaining == 6:  # 나머지가 6일때
        totalcoin += 3  # 2원짜리 동전을 3개 주면
        break  # 전부 거슬러주었기 때문에 while 문도 종료

    elif remaining == 8:  # 나머지가 8일때
        totalcoin += 4  # 2원짜리 동전을 4개 주면
        break  # 전부 거슬러주었기 때문에 while 문도 종료

    elif remaining >= 5:  # 5보다 크면 5원 거슬러 줌
        remaining -= 5  # 앞으로 줘야 할 돈에서 -5
        totalcoin += 1  # 5원짜리 동전 1개 줌
        totalmoney += 5  #총 거슬러준 돈에서 +5

    elif remaining >= 2: # 2보다 크면 2원 거슬러 줌
        remaining -= 2  # 앞으로 줘야 할 돈에서 -5
        totalcoin += 1  # 2원짜리 동전 1개 줌
        totalmoney += 2  #총 거슬러준 돈에서 +2

    else:  # 만약 위에 가능한 경우에 해당이 안되면
        totalcoin = -1  # 거슬러 주기 불가능하니 -1 출력
        break

print(totalcoin)  #거슬러준 동전의 개수 출력
