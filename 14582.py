attack_list = list(map(int, input().split()))
defense_list = list(map(int, input().split()))

attack_num = 0
defense_num = 0

check = False

for i in range(9):
    attack_num += attack_list[i]
    if attack_num > defense_num:
        check = True
    defense_num += defense_list[i]

if attack_num < defense_num and check:
    print("Yes")
else:
    print("No")