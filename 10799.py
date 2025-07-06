import sys
input = sys.stdin.readline

str = input().strip() 
res = 0   # 잘린 쇠막대기의 총 개수
cnt = 0    

for i in range(len(str)):
    if str[i] == "(":  #(이면 새로운 쇠막대기 셍상
        cnt += 1
    else:
        # ')'일 때 
        if str[i-1] == "(": # 바로 앞이 (이면 레이저 쏨
            cnt -= 1   # 레이저로 막대기 하나 끝냄
            res += cnt # 현재 남아있는 막대기 개수만큼 잘린 부분 추가
        else:        
            cnt -= 1  # 막대기 제거
            res += 1  # 제거한 막대기 +1
print(res) 
