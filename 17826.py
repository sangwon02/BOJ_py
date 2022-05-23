li = list(map(int, input().split())) #공백을 기준으로 정수를 리스트에 받음
n = int(input()) #정수를 받음

rank = li.index(n, 0, 50) + 1  #n의 리스트 안에서의 인덱스 + 1을 rank(순위)에 저장

if rank >= 1 and rank <= 5: #1등에서 5등 안이면
    print("A+") #사과
    #밑에 내용은 주석 필요 없을듯?
elif rank >= 6 and rank <= 15:
    print("A0")
elif rank >= 15 and rank <= 30:
    print("B+")
elif rank >= 31 and rank <= 35:
    print("B0")
elif rank >= 36 and rank <= 45:
    print("C+")
elif rank >= 46 and rank <= 48:
    print("C0")
else:
    print("F")
