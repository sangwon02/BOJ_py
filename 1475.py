import sys
input = sys.stdin.readline

s = input().strip()  # 방 번호 입력 받음
cnt = [0] * 10  # 각 숫자의 개수를 넣을 리스트

for i in range(len(s)):
    num = int(s[i])  # i번째 숫자를 확인
    if num == 6 or num == 9:  # 만약 6이나 9면 공유하므로
        if cnt[6] <= cnt[9]:  # 수가 적은 곳에 넣어줌
            cnt[6] += 1
        else:
            cnt[9] += 1
    else:  # 다른 숫자들은 각각 +1
        cnt[num] += 1

print(max(cnt))  # 가장 많은 숫자의 개수 출력