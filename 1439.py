import sys
import math
input = sys.stdin.readline

s = input().strip() 
st = s[0]
cnt = 0

for i in s:
    if st == i: # 만약 전 숫자와 같다면 카운트 안하고
        continue  # 통과
    else:  # 만약 전 숫자와 다르다면
        cnt += 1  # cnt +1
        st = i
        
if cnt == 1:  # 한번만 바뀌었다면
    print(cnt)
else:  # 여러번 바뀌었다면
    print(math.ceil(cnt/2))  # 홀수일 때가 있으니 올림을 해줌