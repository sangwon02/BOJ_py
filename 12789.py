import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

ing = []
now = 1

for num in li: # 리스트를 돌면서
    ing.append(num)  # 일단 대기 줄로 보내고
    
    while ing and ing[-1] == now:  # 간식을 받을 수 있는 경우(순서가 맞는 경우)
        ing.pop() # 간식을 받은 사람 제거하고
        now += 1  # 받을 사람의 번호 +1

if ing:  # 만약 비어있지 않으면
    print("Sad")
else:  # 만약 비어있다면
    print("Nice")