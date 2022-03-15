n = int(input())
car_list = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if car_list[i] != i+1:
        cnt += 1

print(cnt)