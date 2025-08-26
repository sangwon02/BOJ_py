import sys  
input = sys.stdin.readline

n = int(input())

dict = {}  #이모티콘을 사용한 사람을 넣을 딕셔너리
res = 0

for i in range(n):
    st = input().rstrip()
    if st == "ENTER":  # ENTER하면 곰곰 이모티콘을 사용한 사람 초기화
        dict = {}
    elif (st in dict) == False:  # 곰곰 이모티콘을 안쓴 사람이 채팅 치면
        dict[st] = 0
        res += 1  #곰곰 이모티콘 사용횟수 +1
print(res)