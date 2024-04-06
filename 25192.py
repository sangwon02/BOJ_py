import sys  
n = int(sys.stdin.readline())
participants = {}  # 곰곰 이모티콘을 사용한 사람을 넣을 딕셔너리
gomgomcnt = 0

for i in range(n):
    st = input()
    if st == "ENTER":  # ENTER하면 곰곰 이모티콘을 사용한 사람 초기화
        participants = {}
    elif (st in participants) == False:  # 곰곰 이모티콘을 안쓴 사람이 채팅 치면
        participants[st] = 0
        gomgomcnt += 1  #곰곰 이모티콘 사용횟수 +1
    # 곰곰 이모티콘을 사용한 사람이 채팅 치면 아무 일도 안일어남
        
print(gomgomcnt)