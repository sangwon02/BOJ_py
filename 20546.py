import sys
input = sys.stdin.readline

n = int(input())  # 서로 가지게 되는 현금 입력 받음
li = list(map(int, input().split()))  # 날마다의 주식 가격 입력해 리스트에 저장

junstock = 0  # 준성이가 가지고 있는 주식
junmoney = n  # 현재 준현이가 가지고 있는 현금
# 준현의 주식 매매 방법
for i in li: 
    while junmoney >= i:  # 주식을 살 수 없을때 까지 주식 매입
        junstock += 1
        junmoney = junmoney - i
# 마지막 날짜에 준현이가 가지게 되는 돈
junfinal = junmoney + junstock*li[-1]  

sungmoney = n  # 현재 성민이가 가지고 있는 현금
sungstock = 0  # 성민이가 가지고 있는 주식
down = 0  # 주식이 몇일 연속 하락하는지 기록
ascend = 0  # 주식이 몇일 연속 상승하는지 기록

# 성민의 주식 매매 방법
for i in range(len(li)-1):
    if li[i] < li[i+1]:  # 주식이 전날 대비 상승했다면
        ascend += 1  # 연속으로 주식이 오르는 일수 +1
        down = 0  # 주식이 내려가는 일수는 초기화
    elif li[i] > li[i+1]:  # 위에와 반대의 케이스
        ascend = 0
        down += 1
    else:  # 만약 변동이 없다면 전부 초기화
        ascend = 0
        down = 0
    
    # 만약 3일이상 연속으로 가격이 하락했다면 살 수 있을 만큼 주식 매수
    while down >= 3  and sungmoney >= li[i+1]:  
        sungstock += 1
        sungmoney = sungmoney - li[i+1]
    # 만약 3일이상 연속으로 가격이 상승했다면 전부 매도
    while ascend >= 3 and sungstock >= 1:
        sungstock -= 1
        sungmoney = sungmoney + li[i+1]
# 마지막 날짜에 성민이가 가지게 되는 돈
sungfinal = sungmoney + sungstock*li[-1]

# 누가 수익률이 높은지 출력
if junfinal > sungfinal:
    print("BNP")
elif junfinal < sungfinal:
    print("TIMING")
else:
    print("SAMESAME")

